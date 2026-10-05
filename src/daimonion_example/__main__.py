"""Interface for ``python -m daimonion_example``."""

from argparse import ArgumentParser
from collections.abc import Sequence

from . import __version__
from .logging_setup import logger

__all__ = ["main"]


def main(args: Sequence[str] | None = None) -> int | None:
    """Argument parser for the CLI."""
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=__version__,
    )
    parsed = parser.parse_args(args)
    logger.info("daimonion_example_invoked", args=parsed)
    return None


if __name__ == "__main__":
    raise SystemExit(main())
