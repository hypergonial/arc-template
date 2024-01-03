import os

import nox
from nox import options

PATH_TO_PROJECT = os.path.join(".", "src")
SCRIPT_PATHS = [PATH_TO_PROJECT, "noxfile.py"]

# Run the default session via 'nox'
options.sessions = ["format_fix", "pyright"]


# Run me via 'nox -s format_fix'
# Format the code and fix any issues, useful for local development
@nox.session()
def format_fix(session: nox.Session) -> None:
    session.install("-U", "ruff")
    session.run("python", "-m", "ruff", "format", *SCRIPT_PATHS)
    session.run("python", "-m", "ruff", *SCRIPT_PATHS, "--fix")


# Run me via 'nox -s format'
# Checks if the code is formatted correctly, useful for CI
@nox.session()
def format(session: nox.Session) -> None:
    session.install("-U", "ruff")
    session.run("python", "-m", "ruff", "format", *SCRIPT_PATHS, "--check")
    session.run("python", "-m", "ruff", *SCRIPT_PATHS)


# Run me via 'nox -s pyright'
# Runs the pyright static type checker
@nox.session()
def pyright(session: nox.Session) -> None:
    session.install("-r", "requirements.txt")
    session.install("-U", "pyright")
    session.run("pyright", PATH_TO_PROJECT)
