"""Loguru-based logging configuration for DexImitate CLIs."""

import logging
import sys

from loguru import logger


def configure_logging(level: str) -> None:
    """Configure loguru and stdlib root logger to the given level.

    Removes loguru's default handler and installs a fresh one on stderr
    at the requested level, then sets the stdlib root logger to the same
    level so third-party libraries respect the choice.

    Args:
        level: Log level string — one of ``DEBUG``, ``INFO``, ``WARNING``,
            ``ERROR``, or ``CRITICAL`` (case-insensitive).
    """
    level = level.upper()

    # Reset loguru to a clean slate and add a single stderr handler.
    logger.remove()
    logger.add(sys.stderr, level=level)

    # Mirror level on the stdlib root logger so third-party libraries
    # that use ``logging`` are also filtered consistently.
    logging.basicConfig(level=getattr(logging, level, logging.INFO))
