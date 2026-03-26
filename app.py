from database import save_order, get_orders
from utils import calculate_total, format_order, validate_order


DISCOUNT = 10


from dataclasses import dataclass, field
from typing import Optional, List, Dict

@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: float

@dataclass
class OrderDetails:
    order_id: str
    customer_id: str
    items: List[OrderItem]
    shipping_address: str
    billing_address: str
    payment_method: str
    discount_code: Optional[str] = None
    gift_wrap: bool = False
    delivery_date: Optional[str] = None
    special_instructions: Optional[str] = None

def process_order(order_details: OrderDetails):
    """
    Processes a customer order using a consolidated OrderDetails object.
    """
    # Example: Perform initial validation on order_details
    if not order_details.items:
        raise ValueError("Order must contain items.")
    
    print(f"Processing order {order_details.order_id} for customer {order_details.customer_id}...")
    # Example of accessing details:
    # for item in order_details.items:
    #    print(f" - Product: {item.product_id}, Qty: {item.quantity}")
    
    # ... extensive order processing logic using order_details attributes
    
    return {"status": "processed", "order_id": order_details.order_id}
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