"""
Public configuration API for the Snowflake Data Platform project.

This package exposes application configuration, business constants,
error profiles, and logging utilities through a single import location.
"""

from .constants import (
    CUSTOMER_CONSTANTS,
    ORDER_CONSTANTS,
    PAYMENT_CONSTANTS,
    PRODUCT_CONSTANTS,
    SHIPMENT_CONSTANTS,
)
from .error_profiles import (
    CUSTOMER_ERROR_PROFILE,
    ORDER_ERROR_PROFILE,
    PAYMENT_ERROR_PROFILE,
    PRODUCT_ERROR_PROFILE,
    SHIPMENT_ERROR_PROFILE,
)
from .logging_config import get_logger
from .settings import CONFIG

__all__ = [
    "CONFIG",
    "CUSTOMER_CONSTANTS",
    "PRODUCT_CONSTANTS",
    "ORDER_CONSTANTS",
    "PAYMENT_CONSTANTS",
    "SHIPMENT_CONSTANTS",
    "CUSTOMER_ERROR_PROFILE",
    "PRODUCT_ERROR_PROFILE",
    "ORDER_ERROR_PROFILE",
    "PAYMENT_ERROR_PROFILE",
    "SHIPMENT_ERROR_PROFILE",
    "get_logger",
]