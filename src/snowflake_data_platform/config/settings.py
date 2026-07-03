"""
Application configuration for the Snowflake Data Platform project.

This module defines immutable configuration objects used throughout the
application. Configuration is grouped by responsibility to promote
maintainability, scalability, and readability.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from pathlib import Path


# ==============================================================================
# Project Paths
# ==============================================================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]


# ==============================================================================
# Configuration Models
# ==============================================================================


@dataclass(frozen=True, slots=True)
class Settings:
    """General application settings."""

    project_name: str = "Snowflake Data Platform"
    project_version: str = "0.1.0"

    random_seed: int = 42

    default_currency: str = "USD"
    default_encoding: str = "utf-8"


@dataclass(frozen=True, slots=True)
class TableConfig:
    """Configuration for generated dataset sizes."""

    customers: int = 10_000
    products: int = 2_000
    orders: int = 50_000
    payments: int = 50_000
    shipments: int = 45_000

    min_order_items: int = 1
    max_order_items: int = 5


@dataclass(frozen=True, slots=True)
class OutputConfig:
    """Project directory configuration."""

    project_root: Path = PROJECT_ROOT

    data_directory: Path = project_root / "data"

    generated_directory: Path = data_directory / "generated"

    initial_load_directory: Path = generated_directory / "initial_load"

    incremental_directory: Path = generated_directory / "incremental"

    archive_directory: Path = data_directory / "archive"


@dataclass(frozen=True, slots=True)
class DateConfig:
    """Date generation configuration."""

    start_date: str = "2024-01-01"
    end_date: str = "2025-12-31"

    date_format: str = "%Y-%m-%d"
    timestamp_format: str = "%Y-%m-%d %H:%M:%S"


@dataclass(frozen=True, slots=True)
class GenerationConfig:
    """Synthetic data generation configuration."""

    # Dataset sizes
    customers: int = 10_000
    products: int = 500
    orders: int = 75_000
    order_items: int = 225_000
    payments: int = 75_000
    shipments: int = 73_000

    # Generation behaviour
    batch_size: int = 5_000
    max_retries: int = 3

    # Output
    default_file_extension: str = ".csv"

@dataclass(frozen=True, slots=True)
class LoggingConfig:
    """Application logging configuration."""

    level: int = logging.INFO

    file_name: str = "application.log"

    format: str = (
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    )

    date_format: str = "%Y-%m-%d %H:%M:%S"
    
@dataclass(frozen=True, slots=True)
class FileConfig:
    """Output file names."""

    customers: str = "customers.csv"
    products: str = "products.csv"
    orders: str = "orders.csv"
    order_items: str = "order_items.csv"
    payments: str = "payments.csv"
    shipments: str = "shipments.csv"

@dataclass(frozen=True, slots=True)
class AppConfig:
    """
    Root application configuration.

    Provides a single access point to every configuration group.
    """

    settings: Settings = field(default_factory=Settings)
    tables: TableConfig = field(default_factory=TableConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    dates: DateConfig = field(default_factory=DateConfig)
    generation: GenerationConfig = field(default_factory=GenerationConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)
    files: FileConfig = field(default_factory=FileConfig)
# ==============================================================================
# Public Configuration Instance
# ==============================================================================

CONFIG = AppConfig()