from database import save_order, get_orders
from utils import calculate_total, format_order, validate_order


DISCOUNT = 10


def process_order(customer_name, item_name, price, quantity, tax, shipping, coupon):
    if customer_name == "":
        print("customer name empty")
        return None
    if item_name == "":
        print("item name empty")
        return None
    if price < 0:
        print("price invalid")
        return None
    if quantity <= 0:
        print("quantity invalid")
        return None

    if not validate_order(customer_name, item_name, price, quantity):
        return None

    total = calculate_total(price, quantity, tax, shipping, coupon, DISCOUNT)
    order = {
        "customer_name": customer_name,
        "item_name": item_name,
        "price": price,
        "quantity": quantity,
        "tax": tax,
        "shipping": shipping,
        "coupon": coupon,
        "total": total,
    }

    try:
        save_order(order)
    except Exception:
        print("failed to save order")

    return format_order(order)


def main():
    result = process_order("Alice", "Keyboard", 2500, 2, 18, 100, 50)
    print(result)
    print(get_orders())


if __name__ == "__main__":
    main()