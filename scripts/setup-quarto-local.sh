#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
QUARTO_VERSION="${QUARTO_VERSION:-1.7.32}"
QUARTO_DIR="${ROOT_DIR}/.tools/quarto/${QUARTO_VERSION}"
QUARTO_BIN="${QUARTO_DIR}/bin/quarto"
ARCHIVE_PATH="${ROOT_DIR}/.tools/quarto/quarto-${QUARTO_VERSION}-linux-amd64.tar.gz"
DOWNLOAD_URL="https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.tar.gz"

if [[ -x "${QUARTO_BIN}" ]]; then
  echo "${QUARTO_BIN}"
  exit 0
fi

mkdir -p "${ROOT_DIR}/.tools/quarto" "${QUARTO_DIR}"

archive_is_valid() {
  [[ -f "${ARCHIVE_PATH}" ]] && tar -tzf "${ARCHIVE_PATH}" >/dev/null 2>&1
}

if ! archive_is_valid; then
  rm -f "${ARCHIVE_PATH}"
  TMP_ARCHIVE="$(mktemp "${ARCHIVE_PATH}.tmp.XXXXXX")"
  echo "Downloading Quarto ${QUARTO_VERSION}..." >&2
  wget -q -O "${TMP_ARCHIVE}" "${DOWNLOAD_URL}"
  if ! tar -tzf "${TMP_ARCHIVE}" >/dev/null 2>&1; then
    rm -f "${TMP_ARCHIVE}"
    echo "Downloaded Quarto archive is corrupted" >&2
    exit 1
  fi
  mv "${TMP_ARCHIVE}" "${ARCHIVE_PATH}"
fi

rm -rf "${QUARTO_DIR}"
mkdir -p "${QUARTO_DIR}"
tar -xzf "${ARCHIVE_PATH}" -C "${QUARTO_DIR}" --strip-components=1

if [[ ! -x "${QUARTO_BIN}" ]]; then
  echo "Quarto install failed: ${QUARTO_BIN} not found" >&2
  exit 1
fi

echo "${QUARTO_BIN}"
