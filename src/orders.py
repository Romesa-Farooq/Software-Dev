def calculate_items_subtotal(order):
    subtotal = 0

    for item in order["items"]:
        price = item["price"]
        quantity = item["qty"]

        if price > 0:
            if quantity > 0:
                subtotal = subtotal + price * quantity

    return subtotal


def calculate_member_discount(subtotal, member):
    if member == True:
        if subtotal > 100:
            discount_amount = subtotal * 0.2
        else:
            if subtotal > 50:
                discount_amount = subtotal * 0.1
            else:
                discount_amount = 0
    else:
        discount_amount = 0

    return discount_amount


def calculate_shipping_cost(country):
    if country == "PK":
        shipping_cost = 5
    else:
        if country == "US":
            shipping_cost = 15
        else:
            shipping_cost = 25

    return shipping_cost


def calculate_order_total(order):
    subtotal = calculate_items_subtotal(order)
    discount_amount = calculate_member_discount(subtotal, order["member"])
    subtotal = subtotal - discount_amount
    shipping_cost = calculate_shipping_cost(order["country"])
    subtotal = subtotal + shipping_cost

    return subtotal