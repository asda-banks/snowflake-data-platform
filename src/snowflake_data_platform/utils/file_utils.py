"""
File utilities for the Snowflake Data Platform project.

This module provides helper functions for creating output directories
and exporting generated records to CSV files.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

import pandas as pd

import json
from datetime import datetime, timezone

from snowflake_data_platform.config import CONFIG, get_logger

logger = get_logger(__name__)


def create_output_directory(base_directory: Path) -> Path:
    """
    Create a timestamped output directory.

    Parameters
    ----------
    base_directory : Path
        Base directory where the timestamped folder will be created.

    Returns
    -------
    Path
        Path to the created output directory.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    output_directory = base_directory / timestamp

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger.info(
        "Created output directory: %s",
        output_directory,
    )

    return output_directory


def write_csv(
    records: Iterable[Any],
    output_directory: Path,
    file_name: str,
) -> Path:
    """
    Export model objects to a CSV file.

    Parameters
    ----------
    records : Iterable[Any]
        Collection of model objects implementing ``to_dict()``.

    output_directory : Path
        Directory where the CSV file will be written.

    file_name : str
        Name of the CSV file.

    Returns
    -------
    Path
        Path to the generated CSV file.
    """

    output_path = output_directory / file_name

    dataframe = pd.DataFrame(
        record.to_dict()
        for record in records
    )

    dataframe.to_csv(
        output_path,
        index=False,
        encoding=CONFIG.settings.default_encoding,
    )

    logger.info(
        "Exported %s records to %s",
        len(dataframe),
        output_path,
    )

    return output_path

def write_run_metadata(
    output_directory: Path,
    dataset_name: str,
    record_count: int,
    file_name: str,
) -> Path:
    """
    Write execution metadata for a generated dataset.

    Parameters
    ----------
    output_directory : Path
        Directory where the metadata file will be written.

    dataset_name : str
        Name of the generated dataset.

    record_count : int
        Number of generated records.

    file_name : str
        Name of the generated CSV file.

    Returns
    -------
    Path
        Path to the generated metadata file.
    """

    metadata = {
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset": dataset_name,
        "record_count": record_count,
        "file_name": file_name,
        "project_name": CONFIG.settings.project_name,
        "project_version": CONFIG.settings.project_version,
    }

    metadata_path = output_directory / "run_metadata.json"

    with metadata_path.open(
        mode="w",
        encoding=CONFIG.settings.default_encoding,
    ) as file:
        json.dump(
            metadata,
            file,
            indent=4,
        )

    logger.info(
        "Created run metadata: %s",
        metadata_path,
    )

    return metadata_path