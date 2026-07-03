"""
Logging configuration for the Snowflake Data Platform project.

This module provides a centralized logging configuration for the
application. Logs are written to both the console and a log file,
ensuring consistent logging behavior across all modules.
"""

from __future__ import annotations

import logging
from pathlib import Path

from snowflake_data_platform.config.settings import CONFIG


# ==============================================================================
# Logging Configuration
# ==============================================================================

LOG_DIRECTORY: Path = CONFIG.output.project_root / "logs"
LOG_FILE: Path = LOG_DIRECTORY / CONFIG.logging.file_name


def configure_logging() -> None:
    """
    Configure the application's logging.

    This function is safe to call multiple times. Logging is configured
    only once during the application's lifetime.
    """

    # Prevent duplicate handlers if logging has already been configured.
    if logging.getLogger().handlers:
        return

    LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter(
        fmt=CONFIG.logging.format,
        datefmt=CONFIG.logging.date_format,
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(
        filename=LOG_FILE,
        encoding=CONFIG.settings.default_encoding,
    )
    file_handler.setFormatter(formatter)

    logging.basicConfig(
        level=CONFIG.logging.level,
        handlers=[
            console_handler,
            file_handler,
        ],
    )


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.

    Parameters
    ----------
    name : str
        Name of the logger, typically ``__name__``.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    configure_logging()
    return logging.getLogger(name)