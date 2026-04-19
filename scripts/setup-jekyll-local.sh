#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS_DIR="$ROOT_DIR/.tools"
CONDA_ENV_DIR="$TOOLS_DIR/conda-jekyll"
GEM_HOME_DIR="$TOOLS_DIR/bundle"

mkdir -p "$TOOLS_DIR" "$GEM_HOME_DIR"

if ! command -v conda >/dev/null 2>&1; then
  echo "conda is required for local setup but was not found in PATH." >&2
  exit 1
fi

if [[ ! -x "$CONDA_ENV_DIR/bin/ruby" ]]; then
  conda create -y -p "$CONDA_ENV_DIR" -c conda-forge ruby=3.2
fi

if [[ ! -e "$CONDA_ENV_DIR/bin/x86_64-conda-linux-gnu-cc" ]]; then
  ln -sf /usr/bin/gcc "$CONDA_ENV_DIR/bin/x86_64-conda-linux-gnu-cc"
fi

if [[ ! -e "$CONDA_ENV_DIR/bin/x86_64-conda-linux-gnu-c++" ]]; then
  ln -sf /usr/bin/g++ "$CONDA_ENV_DIR/bin/x86_64-conda-linux-gnu-c++"
fi

export PATH="$CONDA_ENV_DIR/bin:$PATH"
export GEM_HOME="$GEM_HOME_DIR"
export GEM_PATH="$GEM_HOME_DIR"
export BUNDLE_PATH="$GEM_HOME_DIR"
export BUNDLE_BIN="$GEM_HOME_DIR/bin"
export PATH="$BUNDLE_BIN:$PATH"

if ! command -v bundler >/dev/null 2>&1 && ! command -v bundle >/dev/null 2>&1; then
  gem install bundler --no-document
fi

bundle check >/dev/null 2>&1 || bundle install

echo
echo "Local Jekyll environment is ready."
echo "Ruby: $("$CONDA_ENV_DIR/bin/ruby" --version)"
echo "Bundle path: $BUNDLE_PATH"
