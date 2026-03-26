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


from dataclasses import dataclass
from typing import List, Optional

@dataclass
class CartItem:
    product_id: str
    price: float
    quantity: int

@dataclass
class CalculationParameters:
    items: List[CartItem]
    tax_rate: float
    discount_percentage: float = 0.0
    shipping_cost: float = 0.0
    gift_wrap_fee: float = 0.0
    handling_fee: float = 0.0
    loyalty_points_redeemed_value: float = 0.0 # Directly store monetary value if applicable

def calculate_total(params: CalculationParameters) -> float:
    """
    Calculates the total cost based on the provided CalculationParameters.
    """
    if not params.items:
        return 0.0 # Or raise an error, depending on business logic
        
    subtotal = sum(item.price * item.quantity for item in params.items)
    
    # Apply discount
    subtotal_after_discount = subtotal * (1 - params.discount_percentage / 100)
    
    # Apply tax
    total_after_tax = subtotal_after_discount * (1 + params.tax_rate / 100)
    
    # Add fixed costs
    final_total = (
        total_after_tax
        + params.shipping_cost
        + params.gift_wrap_fee
        + params.handling_fee
        - params.loyalty_points_redeemed_value
    )

    # Ensure total is not negative, if applicable for business rules
    return max(0.0, round(final_total, 2))
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