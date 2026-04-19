#!/usr/bin/env python3
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path


BASE = "https://scholar.google.com"
PROFILE_ID = "2hUlCnQAAAAJ"
PROFILE_URL = f"{BASE}/citations?user={PROFILE_ID}&hl=en&cstart=0&pagesize=100"
ROOT = Path(__file__).resolve().parents[1]
YAML_PATH = ROOT / "_data" / "publications.yaml"
EQUAL_CONTRIBUTION_AUTHORS = {
    "MaskRIS: Semantic Distortion-aware Data Augmentation for Referring Image Segmentation": [
        "M Lee",
        "S Lee",
    ],
    "CoPatch: Zero-Shot Referring Image Segmentation by Leveraging Untapped Spatial Knowledge in CLIP": [
        "NM An",
        "I Kang",
    ],
    "Threshold matters in wsss: Manipulating the activation for the robust and accurate segmentation model against thresholds": [
        "M Lee",
        "D Kim",
    ],
    "Railroad is not a train: Saliency as pseudo-pixel supervision for weakly supervised semantic segmentation": [
        "M Lee",
        "S Lee",
    ],
    "SeiT++: Masked Token Modeling Improves Storage-efficient Training": [
        "M Lee",
        "S Park",
    ],
    "Saliency as pseudo-pixel supervision for weakly and semi-supervised semantic segmentation": [
        "M Lee",
        "S Lee",
    ],
    "Hybridmatch: Semi-supervised facial landmark detection via hybrid heatmap representations": [
        "S Kang",
        "M Lee",
    ],
    "Psynet: Self-supervised approach to object localization using point symmetric transformation": [
        "K Baek",
        "M Lee",
    ],
    "Fine-Grained Image-Text Correspondence with Cost Aggregation for Open-Vocabulary Part Segmentation": [
        "J Choi",
        "S Lee",
    ],
    "Understanding Multi-Granularity for Open-Vocabulary Part Segmentation": [
        "J Choi",
        "S Lee",
    ],
}
EXCLUDED_TITLES = {
    "Weakly supervised semantic segmentation device and method based on pseudo-masks",
}


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
            href = attrs.get("href", "")
            self.row.cited_by_url = urllib.parse.urljoin(BASE, href) if href else ""
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


def parse_publications(html: str) -> list[Publication]:
    parser = ScholarParser()
    parser.feed(html)
    return [pub for pub in parser.publications if pub.title not in EXCLUDED_TITLES]


def publication_sort_key(pub: Publication) -> tuple[int, str, str]:
    year = extract_year(pub.year or pub.venue or "")
    return (int(year or "0"), pub.venue or "", pub.title or "")


def extract_year(text: str) -> str:
    match = re.search(r"(19|20)\d{2}", text)
    return match.group(0) if match else ""


def emphasize_author(title: str, authors: str) -> str:
    patterns = [r"\bM Lee\b", r"\bMinhyun Lee\b", r"\bLEE Minhyun\b"]
    result = authors
    for pattern in patterns:
        result = re.sub(pattern, lambda m: f"<b>{m.group(0)}</b>", result)

    for name in EQUAL_CONTRIBUTION_AUTHORS.get(title, []):
        candidates = []
        if name == "M Lee":
            candidates = [
                r"<b>M Lee</b>",
                r"<b>Minhyun Lee</b>",
                r"<b>LEE Minhyun</b>",
            ]
        else:
            candidates = [re.escape(name)]

        applied = False
        for candidate in candidates:
            pattern = rf"({candidate})(?!<span class=\"equal-note\">\*</span>)"
            updated = re.sub(pattern, r'\1<span class="equal-note">*</span>', result, count=1)
            if updated != result:
                result = updated
                applied = True
                break

    return result.replace("†", "*")


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def write_outputs(publications: list[Publication]) -> None:
    ordered = sorted(publications, key=publication_sort_key, reverse=True)
    lines = ["papers:", ""]
    for pub in ordered:
        lines.extend(
            [
                f"  - title: {yaml_quote(pub.title)}",
                f"    authors: {yaml_quote(emphasize_author(pub.title, pub.authors))}",
                f"    venue: {yaml_quote(pub.venue)}",
                f"    paper_pdf: {yaml_quote(pub.detail_url)}",
            ]
        )
        if pub.cited_by_url:
            lines.append(f"    cited_by: {yaml_quote(pub.cited_by_url)}")
        lines.append("")

    YAML_PATH.parent.mkdir(parents=True, exist_ok=True)
    YAML_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    html = fetch_profile_html()
    publications = parse_publications(html)

    if not publications:
        print("No publications found.", file=sys.stderr)
        return 1

    write_outputs(publications)
    print(f"Imported {len(publications)} publications into {YAML_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
