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
        return 'auto'
    elif amount <= 1000:
        return 'manager'
    else:
            return 'director'

def apply_discount(price: float, pct: float) -> float:
    """Determine the discount price."""
    return price * (1 - pct / 100)

