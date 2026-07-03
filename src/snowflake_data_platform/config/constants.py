"""
Business domain constants for the Snowflake Data Platform project.

This module contains reference data used during synthetic data generation.
The values represent business master data that would typically exist in an
e-commerce platform.
"""

from __future__ import annotations

from dataclasses import dataclass, field


# ==============================================================================
# Customer Domain
# ==============================================================================


@dataclass(frozen=True, slots=True)
class CustomerConstants:
    """Reference data for customer generation."""

    statuses: tuple[str, ...] = (
        "ACTIVE",
        "INACTIVE",
        "SUSPENDED",
    )

    genders: tuple[str, ...] = (
        "MALE",
        "FEMALE",
        "NON_BINARY",
        "PREFER_NOT_TO_SAY",
    )

    countries: tuple[str, ...] = (
        "United States",
        "Canada",
        "United Kingdom",
        "Germany",
        "France",
        "India",
        "Australia",
        "Singapore",
    )


# ==============================================================================
# Product Domain
# ==============================================================================


@dataclass(frozen=True, slots=True)
class ProductConstants:
    """Reference data for product generation."""

    brands_by_category: dict[str, tuple[str, ...]] = field(
        default_factory=lambda: {
            "Electronics": (
                "Apple",
                "Samsung",
                "Sony",
                "LG",
                "Google",
                "OnePlus",
                "Motorola",
                "Xiaomi",
            ),
            "Computers": (
                "Dell",
                "HP",
                "Lenovo",
                "Asus",
                "Acer",
                "MSI",
                "Microsoft",
            ),
            "Home & Kitchen": (
                "IKEA",
                "KitchenAid",
                "Dyson",
                "Philips",
                "Prestige",
                "Hamilton Beach",
            ),
            "Books": (
                "Penguin",
                "HarperCollins",
                "Hachette",
                "Macmillan",
                "Simon & Schuster",
            ),
            "Fashion": (
                "Nike",
                "Adidas",
                "Puma",
                "Levi's",
                "Zara",
                "H&M",
                "Tommy Hilfiger",
                "Under Armour",
            ),
            "Beauty": (
                "L'Oréal",
                "Maybelline",
                "Nivea",
                "Lakmé",
                "Dove",
                "Neutrogena",
            ),
            "Sports": (
                "Nike",
                "Adidas",
                "Puma",
                "Wilson",
                "Yonex",
                "Decathlon",
            ),
            "Toys": (
                "LEGO",
                "Mattel",
                "Hasbro",
                "Hot Wheels",
                "Nerf",
            ),
            "Groceries": (
                "Nestlé",
                "Kellogg's",
                "PepsiCo",
                "Britannia",
                "Amul",
                "Cadbury",
            ),
        }
    )


# ==============================================================================
# Order Domain
# ==============================================================================


@dataclass(frozen=True, slots=True)
class OrderConstants:
    """Reference data for order generation."""

    statuses: tuple[str, ...] = (
        "PENDING",
        "CONFIRMED",
        "PROCESSING",
        "SHIPPED",
        "DELIVERED",
        "CANCELLED",
        "RETURNED",
    )


# ==============================================================================
# Payment Domain
# ==============================================================================


@dataclass(frozen=True, slots=True)
class PaymentConstants:
    """Reference data for payment generation."""

    methods: tuple[str, ...] = (
        "Credit Card",
        "Debit Card",
        "UPI",
        "Net Banking",
        "PayPal",
        "Digital Wallet",
        "Cash on Delivery",
    )

    statuses: tuple[str, ...] = (
        "PENDING",
        "SUCCESS",
        "FAILED",
        "REFUNDED",
    )


# ==============================================================================
# Shipment Domain
# ==============================================================================


@dataclass(frozen=True, slots=True)
class ShipmentConstants:
    """Reference data for shipment generation."""

    methods: tuple[str, ...] = (
        "Standard",
        "Express",
        "Same Day",
        "Store Pickup",
    )

    statuses: tuple[str, ...] = (
        "PENDING",
        "IN_TRANSIT",
        "OUT_FOR_DELIVERY",
        "DELIVERED",
        "RETURNED",
    )


# ==============================================================================
# Public Constant Objects
# ==============================================================================

CUSTOMER_CONSTANTS = CustomerConstants()
PRODUCT_CONSTANTS = ProductConstants()
ORDER_CONSTANTS = OrderConstants()
PAYMENT_CONSTANTS = PaymentConstants()
SHIPMENT_CONSTANTS = ShipmentConstants()