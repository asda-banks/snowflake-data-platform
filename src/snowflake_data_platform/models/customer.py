"""
Customer data model.

This module defines the canonical customer schema used throughout the
Snowflake Data Platform project.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import date, datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class Customer:
    """Represents a customer record."""

    customer_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    gender: str
    date_of_birth: date
    country: str
    city: str
    postal_code: str
    address: str
    customer_status: str
    created_at: datetime
    updated_at: datetime

    @property
    def full_name(self) -> str:
        """
        Return the customer's full name.

        Returns
        -------
        str
            Full name in the format "FirstName LastName".
        """
        return f"{self.first_name} {self.last_name}"

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the customer record to a dictionary.

        Returns
        -------
        dict[str, Any]
            Dictionary representation of the customer.
        """
        return asdict(self)