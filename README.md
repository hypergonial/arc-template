# arc-template

A template to start creating a bot using hikari-arc. To see a Gateway version of this template, see the [`gateway` branch](https://github.com/hypergonial/arc-template/tree/gateway) of this repository.

## Setting up

Create your repository using this template, clone/download it, then install all requirements:

```sh
pip install -r requirements.txt -r dev_requirements.txt
```

This will install:

- [hikari-arc](https://github.com/hypergonial/hikari-arc) and all it's dependencies
- [python-dotenv](https://github.com/theskumar/python-dotenv) to handle `.env` files
- [ruff](https://github.com/astral-sh/ruff) a Python formatter and linter to help keep your code tidy
- [pyright](https://github.com/microsoft/pyright) a Python typechecker to ensure correctness & type-safety
- [nox](https://github.com/wntrblm/nox) a Python session runner to automate running the previous two tools

## Learning `arc`

- [Documentation](https://arc.hypergonial.com)
- [Examples](https://github.com/hypergonial/hikari-arc/tree/main/examples)
- [Discord Server](https://discord.gg/hikari)

## Running the bot

To run the bot, run the following command in the project folder:

```sh
python3 -m src
# On Windows you may need to do:
py -m src
```

## Tooling

### nox

`nox` is a tool that can set up & run automated sessions. This template ships with the following session:

`format_fix` - Run `ruff` to format & fix code (where possible) - default
`format` - Run `ruff` to check for formatting & code correctness issues
`pyright` - Run `pyright` to typecheck the code - default

To run a nox session, use `nox -s session_name`, so for example, to run `pyright`, use `nox -s pyright`.
You can also run the default set of sessions using `nox`.

### Configuration

All of the tooling is configured using [`pyproject.toml`](https://github.com/hypergonial/arc-template/blob/gateway/pyproject.toml), see that file for more information!

### Editor support

#### VS Code

If you're using **Visual Studio Code**, you should automatically **get a prompt** when you first open the project to install
recommended extensions. The recommended extensions include:

- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - Python Language Support
- [Ruff](https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff) - Run ruff while you edit!
- [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) - Generate new docstrings
- [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) - Respect `.editorconfig`
- [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) - `.toml` file support

Installing these will make your developer experience better, as pyright & ruff will be able to run on your code while you edit it!

> If you've dismissed the prompt, you can see & install the recommended extensions by searching for `@recommended` in the Extensions panel.

In addition, you can run `nox` using the shortcut `Ctrl` + `Shift` + `B`.

#### PyCharm

PyCharm should respect `.editorconfig` out of the box. Unfortunately I'm not aware of any good extensions that would allow it to run `ruff` while code
is being edited. You can use `nox` for this purpose as a placeholder.

#### Other editors

If you'd like to see explicit support for more editors in this template, please open a [pull request](https://github.com/hypergonial/arc-template/pulls).
