from typing import Any


def calculate_items_subtotal(order: dict[str, Any]) -> float:
    subtotal = 0.0

    for item in order["items"]:
        price = item["price"]
        quantity = item["qty"]

        if price <= 0:
            continue

        if quantity <= 0:
            continue

        subtotal = subtotal + price * quantity

    return subtotal


def calculate_member_discount(subtotal: float, member: bool) -> float:
    if not member:
        return 0.0

    if subtotal > 100:
        return subtotal * 0.2

    if subtotal > 50:
        return subtotal * 0.1

    return 0.0


def calculate_shipping_cost(country: str) -> int:
    if country == "PK":
        return 5

    if country == "US":
        return 15

    return 25


def calculate_order_total(order: dict[str, Any]) -> float:
    subtotal = calculate_items_subtotal(order)

    discount_amount = calculate_member_discount(
        subtotal,
        order["member"]
    )

    subtotal = subtotal - discount_amount

    shipping_cost = calculate_shipping_cost(order["country"])

    subtotal = subtotal + shipping_cost

    return subtotal