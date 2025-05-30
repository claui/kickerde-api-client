# Contributing to the API client for kicker.de

## Setting up the library for development

To set up the API client for kicker.de, you need three things:

1. The Python version manager `pyenv`.

2. A system-wide Python installation.

3. The Python dependency manager `poetry`.

### Installing pyenv

The Python version manager `pyenv` makes sure you can always keep
the exact Python version required by the API client for kicker.de,
regardless of your system Python.

#### Installing pyenv on Windows

While `pyenv` doesn’t support Windows, you can use a drop-in
replacement called `pyenv-win`.

To install `pyenv-win` on Windows, go to
[github.com/pyenv-win/pyenv-win](https://github.com/pyenv-win/pyenv-win#installation)
and follow one of the installation methods.

#### Installing pyenv on Linux

To install `pyenv` on Linux or WSL2, first make sure Python 3 is
installed. Then follow the _Basic GitHub Checkout_ method described
at [github.com/pyenv/pyenv](https://github.com/pyenv/pyenv#basic-github-checkout).

#### Installing pyenv on macOS

To install `pyenv` on macOS, run:

```shell
brew install pyenv
```

#### Checking your system-wide pyenv installation

To verify your `pyenv` is working, run:

```shell
pyenv --version
```

### Checking your system-wide Python installation

Make sure you have Python 3.8 or higher installed on your system
and available in your PATH.

To check, run:

```shell
python --version
```

If that fails, try:

```shell
python3 --version
```

Proceed after you’ve confirmed one of those to work.

### Installing Poetry

You’ll need `poetry` to manage development dependencies and the venv.

To install Poetry on Windows, use one of the
[installation methods](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
described in Poetry’s documentation.

To install Poetry on macOS, run:

```shell
brew install poetry
```

If you’re on Linux or WSL2, use your system package manager to
install Poetry.

Alternatively, use one of the
[installation methods](https://python-poetry.org/docs/master/#installing-with-the-official-installer)
described in Poetry’s documentation.

#### Checking your Poetry installation

To verify Poetry is working, run:

```shell
poetry --version
```

### Setting up your virtual environment

To set up your virtual environment, follow these steps:

1. Go to the project root directory.

2. Run `pyenv install -s`.

3. Run `pyenv exec python -m venv .venv`.

4. Run `poetry install`.

You need to do the above steps only once.

To update your dependencies after a `git pull`, run `poetry update`.

## Development scripts and tasks

To see a list of available tasks, run: `poetry run poe tasks`

### Running the tests

To execute the tests, run:

```shell
poetry run poe tests
```

To execute a single test, run e. g.:

```shell
poetry run poe tests -vv tests/test_leagues.py::test_friendlies
```

### Running the linter

To execute the linter, run:

```shell
poetry run poe linter
```

### Running the code formatting style check

To check the code base for formatting style violations that are not
covered by the linter, run:

```shell
poetry run poe formatcheck
```

### Running the static type check

To execute the static type check, run:

```shell
poetry run poe typecheck
```

### Running the entire CI pipeline locally

If you have [act](https://github.com/nektos/act) installed and a
Docker daemon active, run:

```shell
act
```

### Generating project documentation

To generate project documentation, run:

```shell
poetry run poe doc
```

To open the generated HTML documentation in your browser, run:

```shell
poetry run poe html
```

## Maintenance

### Refreshing dependencies

If you get errors after a Git pull, refresh your dependencies:

```shell
poetry update
```

### Rebuilding the virtual environment

If you’ve run `poetry update` and you still get errors, rebuild
the virtual environment:

```shell
poetry install
```

### Checking dependencies for compatible updates

To check dependencies for compatible updates, run:

```shell
poetry update --dry-run
```

### Updating requirements file for Read the Docs

To update the `doc/requirements.txt` file for Read the Docs, run:

```shell
poetry export --only doc --output doc/requirements.txt
```
