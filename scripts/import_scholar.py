#!/usr/bin/env python3

import json
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


BASE = "https://scholar.google.com"
PROFILE_ID = "2hUlCnQAAAAJ"
PROFILE_URL = f"{BASE}/citations?user={PROFILE_ID}&hl=en&cstart=0&pagesize=100"
ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "publications.json"
PAGE_PATH = ROOT / "publications.qmd"


@dataclass
class Publication:
    title: str = ""
    authors: str = ""
    venue: str = ""
    year: str = ""
    citations: str = ""
    detail_url: str = ""
    cited_by_url: str = ""


class ScholarParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.publications: list[Publication] = []
        self.in_row = False
        self.row: Publication | None = None
        self.capture: str | None = None
        self.gray_index = 0
        self.buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        attrs = dict(attrs)

        if tag == "tr" and attrs.get("class") == "gsc_a_tr":
            self.in_row = True
            self.row = Publication()
            self.gray_index = 0
            return

        if not self.in_row or self.row is None:
            return

        if tag == "a" and attrs.get("class") == "gsc_a_at":
            self.row.detail_url = urllib.parse.urljoin(BASE, attrs.get("href", ""))
            self.capture = "title"
            self.buffer = []
            return

        if tag == "div" and attrs.get("class") == "gs_gray":
            self.capture = "gray"
            self.buffer = []
            return

        if tag == "a" and "gsc_a_ac" in attrs.get("class", ""):
            self.row.cited_by_url = attrs.get("href", "")
            self.capture = "citations"
            self.buffer = []
            return

        if tag == "span" and "gsc_a_h" in attrs.get("class", ""):
            self.capture = "year"
            self.buffer = []

    def handle_endtag(self, tag: str) -> None:
        if not self.in_row or self.row is None:
            return

        if tag == "a" and self.capture == "title":
            self.row.title = clean("".join(self.buffer))
            self.capture = None
            self.buffer = []
            return

        if tag == "div" and self.capture == "gray":
            value = clean("".join(self.buffer))
            if self.gray_index == 0:
                self.row.authors = value
            elif self.gray_index == 1:
                self.row.venue = value
            self.gray_index += 1
            self.capture = None
            self.buffer = []
            return

        if tag == "a" and self.capture == "citations":
            self.row.citations = clean("".join(self.buffer))
            self.capture = None
            self.buffer = []
            return

        if tag == "span" and self.capture == "year":
            self.row.year = clean("".join(self.buffer))
            self.capture = None
            self.buffer = []
            return

        if tag == "tr":
            if self.row.title:
                self.publications.append(self.row)
            self.in_row = False
            self.row = None
            self.capture = None
            self.buffer = []

    def handle_data(self, data: str) -> None:
        if self.capture is not None:
            self.buffer.append(data)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", unescape(text)).strip()


def fetch_profile_html() -> str:
    request = urllib.request.Request(PROFILE_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", "ignore")


def parse_profile_meta(html: str) -> dict[str, str]:
    title_match = re.search(r"<title>(.*?)</title>", html, re.S)
    desc_match = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
    description = clean(desc_match.group(1)) if desc_match else ""
    description_parts = [part.strip() for part in description.split(" - ") if part.strip()]
    description_parts = [part for part in description_parts if "cited by" not in part.lower()]
    return {
        "title": clean(title_match.group(1)) if title_match else "Minhyun Lee - Google Scholar",
        "description": " - ".join(description_parts),
    }


def parse_publications(html: str) -> list[Publication]:
    parser = ScholarParser()
    parser.feed(html)
    return parser.publications


def write_json(publications: list[Publication]) -> None:
    DATA_PATH.write_text(
        json.dumps([asdict(pub) for pub in publications], ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_publications_page(meta: dict[str, str], publications: list[Publication]) -> None:
    selected = publications[:4]
    grouped = group_publications(publications)
    lines = [
        "---",
        'title: "Publications"',
        "---",
        "",
        "## Overview",
        "",
        "A curated list generated from the public Google Scholar profile and organized by publication type.",
        "",
        f"Source: [Google Scholar profile]({PROFILE_URL})",
        "",
        "## Selected Publications",
        "",
    ]

    for pub in selected:
        lines.extend(format_publication(pub, level="###"))

    lines.extend(
        [
            "",
            "## Full List",
            "",
        ]
    )

    if meta["description"]:
        lines.extend(
            [
                f"Profile: {meta['description']}",
                "",
            ]
        )

    lines.extend(
        [
            f"Total entries imported: {len(publications)}",
            "",
        ]
    )

    section_order = ["Conference", "Journal", "Preprint", "Patent", "Other"]
    headings = {
        "Conference": "### Conference Papers",
        "Journal": "### Journal Articles",
        "Preprint": "### Preprints",
        "Patent": "### Patents",
        "Other": "### Other",
    }

    for key in section_order:
        items = grouped.get(key, [])
        if not items:
            continue
        lines.extend([headings[key], ""])
        for pub in items:
            lines.extend(format_publication(pub, level="####"))

    PAGE_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_publication(pub: Publication, level: str) -> list[str]:
    title_link = f"[{pub.title}]({pub.detail_url})" if pub.detail_url else pub.title
    details = " | ".join(part for part in [pub.authors, pub.venue] if part)
    block = [
        f"{level} {title_link}",
        "",
    ]
    if details:
        block.append(details)
        block.append("")
    show_year_line = bool(pub.year) and (not pub.venue or pub.year not in pub.venue)
    if show_year_line:
        block.append(pub.year)
        block.append("")
    return block


def publication_kind(pub: Publication) -> str:
    text = f"{pub.venue} {pub.title}".lower()
    if "patent" in text:
        return "Patent"
    if "arxiv" in text or "preprint" in text or "ssrn" in text:
        return "Preprint"
    if any(token in text for token in ["transactions", "journal", "ieee access", "tmlr", "pattern analysis and machine intelligence"]):
        return "Journal"
    if any(token in text for token in ["conference", "cvpr", "eccv", "neurips", "aaai", "iccv"]):
        return "Conference"
    return "Other"


def group_publications(publications: list[Publication]) -> dict[str, list[Publication]]:
    grouped: dict[str, list[Publication]] = {
        "Conference": [],
        "Journal": [],
        "Preprint": [],
        "Patent": [],
        "Other": [],
    }
    for pub in publications:
        grouped[publication_kind(pub)].append(pub)
    return grouped


def main() -> int:
    html = fetch_profile_html()
    meta = parse_profile_meta(html)
    publications = parse_publications(html)

    if not publications:
        print("No publications found.", file=sys.stderr)
        return 1

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_json(publications)
    write_publications_page(meta, publications)
    print(f"Imported {len(publications)} publications into {PAGE_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
