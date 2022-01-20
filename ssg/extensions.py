import importlib
import sys
from pathlib import Path


def load_module(directory, name):
    """Dir from which to load extension, name of the module."""
    sys.path.insert(0, directory)

    # Dynamically load the module.
    importlib.import_module(name)

    # Remove the dynamically added path.
    sys.path.pop(0)


def load_directory(directory):
    for path in directory.rglob("*.py"):
        load_module(directory.as_posix(), path.stem)


def load_bundled():
    directory = Path(__path__).parent / "extensions"
    load_directory(directory)
