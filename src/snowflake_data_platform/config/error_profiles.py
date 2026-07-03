"""
Data quality error profiles for the Snowflake Data Platform project.

This module defines configurable error probabilities used to inject
realistic data quality issues into the generated datasets.

Each value represents the probability (0.0 - 1.0) that a particular
error will be introduced during data generation.
"""

from __future__ import annotations

from dataclasses import dataclass


# ==============================================================================
# Customer Error Profile
# ==============================================================================


@dataclass(frozen=True, slots=True)
class CustomerErrorProfile:
    """Data quality rules for customer records."""

    missing_email: float = 0.02
    duplicate_email: float = 0.005
    invalid_phone_number: float = 0.01
    missing_country: float = 0.005
    invalid_postal_code: float = 0.003
    leading_trailing_spaces: float = 0.01
    mixed_case_name: float = 0.01


# ==============================================================================
# Product Error Profile
# ==============================================================================


@dataclass(frozen=True, slots=True)
class ProductErrorProfile:
    """Data quality rules for product records."""

    missing_brand: float = 0.005
    missing_category: float = 0.003
    duplicate_sku: float = 0.002
    negative_price: float = 0.002
    zero_price: float = 0.001
    invalid_category: float = 0.002
    leading_trailing_spaces: float = 0.01


# ==============================================================================
# Order Error Profile
# ==============================================================================


@dataclass(frozen=True, slots=True)
class OrderErrorProfile:
    """Data quality rules for order records."""

    future_order_date: float = 0.003
    duplicate_order: float = 0.002
    missing_customer_id: float = 0.002
    invalid_customer_id: float = 0.003
    invalid_order_status: float = 0.002


# ==============================================================================
# Payment Error Profile
# ==============================================================================


@dataclass(frozen=True, slots=True)
class PaymentErrorProfile:
    """Data quality rules for payment records."""

    amount_mismatch: float = 0.005
    missing_payment_method: float = 0.003
    failed_payment: float = 0.02
    duplicate_payment: float = 0.002


# ==============================================================================
# Shipment Error Profile
# ==============================================================================


@dataclass(frozen=True, slots=True)
class ShipmentErrorProfile:
    """Data quality rules for shipment records."""

    missing_tracking_number: float = 0.005
    invalid_tracking_number: float = 0.003
    delayed_shipment: float = 0.02
    future_delivery_date: float = 0.003
    invalid_shipment_status: float = 0.002


# ==============================================================================
# Public Error Profile Objects
# ==============================================================================

CUSTOMER_ERROR_PROFILE = CustomerErrorProfile()

PRODUCT_ERROR_PROFILE = ProductErrorProfile()

ORDER_ERROR_PROFILE = OrderErrorProfile()

PAYMENT_ERROR_PROFILE = PaymentErrorProfile()

SHIPMENT_ERROR_PROFILE = ShipmentErrorProfile()