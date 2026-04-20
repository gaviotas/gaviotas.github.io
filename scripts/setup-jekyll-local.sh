#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS_DIR="$ROOT_DIR/.tools"
CONDA_ENV_DIR="$TOOLS_DIR/conda-jekyll"
GEM_HOME_DIR="$TOOLS_DIR/bundle"
BREW_RUBY_FORMULA="ruby@3.2"
BUNDLER_VERSION="$(awk '/^BUNDLED WITH$/{getline; gsub(/^[[:space:]]+/, ""); print; exit}' "$ROOT_DIR/Gemfile.lock")"

mkdir -p "$TOOLS_DIR" "$GEM_HOME_DIR"

RUBY_BIN=""
RUBY_SOURCE=""

if command -v conda >/dev/null 2>&1; then
  if [[ ! -x "$CONDA_ENV_DIR/bin/ruby" ]]; then
    conda create -y -p "$CONDA_ENV_DIR" -c conda-forge ruby=3.2
  fi

  if [[ "$OSTYPE" == linux* ]]; then
    if [[ ! -e "$CONDA_ENV_DIR/bin/x86_64-conda-linux-gnu-cc" ]]; then
      ln -sf /usr/bin/gcc "$CONDA_ENV_DIR/bin/x86_64-conda-linux-gnu-cc"
    fi

    if [[ ! -e "$CONDA_ENV_DIR/bin/x86_64-conda-linux-gnu-c++" ]]; then
      ln -sf /usr/bin/g++ "$CONDA_ENV_DIR/bin/x86_64-conda-linux-gnu-c++"
    fi
  fi

  RUBY_BIN="$CONDA_ENV_DIR/bin/ruby"
  RUBY_SOURCE="conda"
elif command -v brew >/dev/null 2>&1; then
  if ! brew list "$BREW_RUBY_FORMULA" >/dev/null 2>&1; then
    brew install "$BREW_RUBY_FORMULA"
  fi

  RUBY_BIN="$(brew --prefix "$BREW_RUBY_FORMULA")/bin/ruby"
  RUBY_SOURCE="homebrew"
else
  echo "Neither conda nor Homebrew is available, so local Ruby setup cannot continue." >&2
  exit 1
fi

export PATH="$(dirname "$RUBY_BIN"):$PATH"
export GEM_HOME="$GEM_HOME_DIR"
export GEM_PATH="$GEM_HOME_DIR"
export BUNDLE_PATH="$GEM_HOME_DIR"
export BUNDLE_BIN="$GEM_HOME_DIR/bin"
export PATH="$BUNDLE_BIN:$PATH"

if [[ -n "$BUNDLER_VERSION" ]] && ! bundle _"$BUNDLER_VERSION"_ --version >/dev/null 2>&1; then
  gem install bundler -v "$BUNDLER_VERSION" --no-document
elif ! command -v bundler >/dev/null 2>&1 && ! command -v bundle >/dev/null 2>&1; then
  gem install bundler --no-document
fi

if ! bundle lock --add-platform arm64-darwin >/dev/null 2>&1 && ! bundle lock --add-platform "$(ruby -e 'print Gem::Platform.local.to_s')" >/dev/null 2>&1; then
  true
fi

bundle _"$BUNDLER_VERSION"_ check >/dev/null 2>&1 || bundle _"$BUNDLER_VERSION"_ install

echo
echo "Local Jekyll environment is ready."
echo "Ruby source: $RUBY_SOURCE"
echo "Ruby: $("$RUBY_BIN" --version)"
echo "Bundle path: $BUNDLE_PATH"
