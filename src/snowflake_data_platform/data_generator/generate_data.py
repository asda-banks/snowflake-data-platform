"""
Synthetic data generation entry point.

This module orchestrates the generation of synthetic datasets.
"""

from __future__ import annotations

from snowflake_data_platform.config import CONFIG, get_logger
from snowflake_data_platform.data_generator.generators.customers import (
    CustomerGenerator,
)
from snowflake_data_platform.utils.file_utils import (
    create_output_directory,
    write_csv,
)
from snowflake_data_platform.utils.file_utils import (
    create_output_directory,
    write_csv,
    write_run_metadata,
)

logger = get_logger(__name__)


def main() -> None:
    """
    Generate all datasets for the initial data load.
    """

    logger.info("Starting synthetic data generation.")

    output_directory = create_output_directory(
        CONFIG.output.initial_load_directory,
    )

    customers = CustomerGenerator().generate()

    write_csv(
        records=customers,
        output_directory=output_directory,
        file_name=CONFIG.files.customers,
    )
    write_run_metadata(
        output_directory=output_directory,
        dataset_name="customers",
        record_count=len(customers),
        file_name=CONFIG.files.customers,
    )

    logger.info("Synthetic data generation completed successfully.")


if __name__ == "__main__":
    main()