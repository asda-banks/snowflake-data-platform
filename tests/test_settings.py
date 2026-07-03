from snowflake_data_platform.config import (
    CONFIG,
    CUSTOMER_CONSTANTS,
    CUSTOMER_ERROR_PROFILE,
    get_logger,
)

logger = get_logger(__name__)


def main() -> None:
    logger.info("Configuration test started.")

    print(CONFIG.settings.project_name)
    print(CONFIG.tables.customers)
    print(CUSTOMER_CONSTANTS.statuses)
    print(CUSTOMER_ERROR_PROFILE.missing_email)

    logger.info("Configuration test completed.")


if __name__ == "__main__":
    main()