def validate_order(customer_name, item_name, price, quantity):
    if customer_name is None:
        return False
    if item_name is None:
        return False
    if price is None:
        return False
    if quantity is None:
        return False
    if customer_name == "":
        return False
    if item_name == "":
        return False
    if price < 0:
        return False
    if quantity <= 0:
        return False
    return True


def calculate_total(price, quantity, tax, shipping, coupon, discount):
    subtotal = price * quantity
    total = subtotal + tax + shipping
    total = total - coupon
    total = total - discount
    return total


def format_order(order):
    return (
        "Customer: " + str(order["customer_name"])
        + ", Item: " + str(order["item_name"])
        + ", Total: " + str(order["total"])
    )