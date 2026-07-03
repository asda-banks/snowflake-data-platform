"""
Customer data generator.

This module generates synthetic customer records using the project's
configuration, constants, and utility modules.
"""

from __future__ import annotations

from datetime import datetime, timezone

from snowflake_data_platform.config import (
    CONFIG,
    CUSTOMER_CONSTANTS,
    get_logger,
)
from snowflake_data_platform.models.customer import Customer
from snowflake_data_platform.utils.fake_data import FAKE_DATA
from snowflake_data_platform.utils.id_generator import (
    generate_customer_id,
)

logger = get_logger(__name__)


class CustomerGenerator:
    """Generates synthetic customer records."""

    def generate(self, count: int | None = None) -> list[Customer]:
        """
        Generate customer records.

        Parameters
        ----------
        count : int | None, optional
            Number of customer records to generate.
            If omitted, the configured default is used.

        Returns
        -------
        list[Customer]
            Generated customer records.
        """

        if count is None:
            count = CONFIG.generation.customers

        logger.info("Generating %s customer records...", count)

        customers = [
            self._generate_customer()
            for _ in range(count)
        ]

        logger.info(
            "Successfully generated %s customer records.",
            len(customers),
        )

        return customers

    def _generate_customer(self) -> Customer:
        """
        Generate a single customer record.

        Returns
        -------
        Customer
            Generated customer.
        """

        first_name = FAKE_DATA.first_name()
        last_name = FAKE_DATA.last_name()

        timestamp = datetime.now(timezone.utc)

        return Customer(
            customer_id=generate_customer_id(),
            first_name=first_name,
            last_name=last_name,
            email=FAKE_DATA.email(),
            phone_number=FAKE_DATA.phone_number(),
            gender=FAKE_DATA.random_choice(
                CUSTOMER_CONSTANTS.genders,
            ),
            date_of_birth=FAKE_DATA.date_of_birth(),
            country=FAKE_DATA.random_choice(
                CUSTOMER_CONSTANTS.countries,
            ),
            city=FAKE_DATA.city(),
            postal_code=FAKE_DATA.postal_code(),
            address=FAKE_DATA.address(),
            customer_status=FAKE_DATA.random_choice(
                CUSTOMER_CONSTANTS.statuses,
            ),
            created_at=timestamp,
            updated_at=timestamp,
        )