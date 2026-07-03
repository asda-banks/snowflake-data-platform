"""
Identifier generation utilities.

This module provides entity-specific identifier generators used throughout
the Snowflake Data Platform project.

Currently, all identifiers are UUID4 strings. Keeping separate generator
functions for each business entity allows future changes to ID formats
without affecting the rest of the application.
"""

from __future__ import annotations

from uuid import uuid4


def generate_customer_id() -> str:
    """
    Generate a unique customer identifier.

    Returns
    -------
    str
        Customer identifier.
    """
    return str(uuid4())


def generate_product_id() -> str:
    """
    Generate a unique product identifier.

    Returns
    -------
    str
        Product identifier.
    """
    return str(uuid4())


def generate_order_id() -> str:
    """
    Generate a unique order identifier.

    Returns
    -------
    str
        Order identifier.
    """
    return str(uuid4())


def generate_order_item_id() -> str:
    """
    Generate a unique order item identifier.

    Returns
    -------
    str
        Order item identifier.
    """
    return str(uuid4())


def generate_payment_id() -> str:
    """
    Generate a unique payment identifier.

    Returns
    -------
    str
        Payment identifier.
    """
    return str(uuid4())


def generate_shipment_id() -> str:
    """
    Generate a unique shipment identifier.

    Returns
    -------
    str
        Shipment identifier.
    """
    return str(uuid4())