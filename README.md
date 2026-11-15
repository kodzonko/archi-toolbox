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

## Test coverage

GitHub Actions runs the tests and uploads branch coverage to
[Codecov](https://app.codecov.io/gh/kodzonko/archi-toolbox) on pushes and pull requests.
Uploads use GitHub OIDC and need no `CODECOV_TOKEN` secret; upload errors fail CI.

```sh
uv run --locked pytest --cov=archi_toolbox --cov-branch --cov-report=term-missing --cov-report=xml:coverage.xml
```
