# Archi Toolbox

## Tool setup

Install [mise](https://mise.jdx.dev/getting-started.html), then run from the repository root:

```sh
mise trust
mise install
```

Tool versions are declared in `mise.toml`. Activate mise in your shell, or prefix
project commands with `mise exec --` (for example, `mise exec -- uv --version`).

Install dependencies with `mise exec -- uv sync --locked`. SVG rendering still
requires system Cairo and pkg-config (on macOS: `brew install cairo pkgconf`).
