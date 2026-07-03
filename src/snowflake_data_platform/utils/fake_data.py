"""
Utility functions for generating synthetic data.

This module provides a centralized wrapper around the Faker library,
ensuring consistent fake data generation across the project.
"""

from __future__ import annotations

from datetime import date
from typing import Sequence, TypeVar

from faker import Faker

T = TypeVar("T")


class FakeData:
    """Wrapper around the Faker library."""

    def __init__(
        self,
        locale: str = "en_US",
        seed: int | None = None,
    ) -> None:
        """
        Initialize the fake data generator.

        Parameters
        ----------
        locale : str, optional
            Faker locale, by default "en_US".

        seed : int | None, optional
            Seed used to generate deterministic fake data.
            If None, random data is generated.
        """
        self._locale = locale
        self._seed = seed
        self._faker = Faker(locale)

        if seed is not None:
            self._faker.seed_instance(seed)

    def first_name(self) -> str:
        """Generate a first name."""
        return self._faker.first_name()

    def last_name(self) -> str:
        """Generate a last name."""
        return self._faker.last_name()

    def full_name(self) -> str:
        """Generate a full name."""
        return self._faker.name()

    def email(self) -> str:
        """Generate an email address."""
        return self._faker.email()

    def phone_number(self) -> str:
        """Generate a phone number."""
        return self._faker.phone_number()

    def address(self) -> str:
        """Generate a street address."""
        return self._faker.street_address()

    def city(self) -> str:
        """Generate a city."""
        return self._faker.city()

    def postal_code(self) -> str:
        """Generate a postal code."""
        return self._faker.postcode()

    def date_of_birth(
        self,
        minimum_age: int = 18,
        maximum_age: int = 80,
    ) -> date:
        """
        Generate a realistic date of birth.

        Parameters
        ----------
        minimum_age : int
            Minimum customer age.

        maximum_age : int
            Maximum customer age.

        Returns
        -------
        date
            Randomly generated date of birth.
        """
        return self._faker.date_of_birth(
            minimum_age=minimum_age,
            maximum_age=maximum_age,
        )

    def random_choice(self, values: Sequence[T]) -> T:
        """
        Return a random element from a sequence.

        Parameters
        ----------
        values : Sequence[T]
            Collection of values.

        Returns
        -------
        T
            Randomly selected value.
        """
        return self._faker.random_element(values)


# ==============================================================================
# Public Instance
# ==============================================================================

FAKE_DATA = FakeData()