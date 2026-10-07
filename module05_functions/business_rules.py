# business_rules.py
# Author: Mateus De Mesquita

APPROVAL_LIMIT = 1000


def calculate_total(price: float, quantity: int) -> float:
    """Return total cost including 7% tax."""
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Determine if the total price exceeds our approval limit."""
    return amount > APPROVAL_LIMIT


def get_approval_tier(amount: float) -> str:
    """Determine which tier of leadership is necessary for approval."""
    if amount <= 500:
        return "auto"
    elif amount <= 1000:
        return "manager"
    else:
        return "director"


def apply_discount(price: float, pct: float) -> float:
    """Determine the discount price."""
    return price * (1 - pct / 100)


# add sample inputs
price, qty = 450.00, 3
total = calculate_total(price, qty)
review = requires_review(total)
tier = get_approval_tier(total)
discounted_price = apply_discount(price, 10)

print(f"Total cost: ${total:.2f}")
print(f"Requires review: {review}")
print(f"Approval tier: {tier}")
print(f"10% discount: ${discounted_price:.2f}")
