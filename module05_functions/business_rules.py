"""Business rules for laptop purchases."""

APPROVAL_LIMIT = 1000


def calculate_total(price: float, quantity: int) -> float:
    """Return the total laptop cost including 7% tax."""
    return price * quantity * 1.07


def requires_review(amount: float) -> bool:
    """Return True if the purchase exceeds the approval limit."""
    return amount > APPROVAL_LIMIT


def get_approval_tier(amount: float) -> str:
    """Return the approval tier based on purchase amount."""
    if amount <= 500:
        return "auto"
    elif amount <= 2000:
        return "manager"
    else:
        return "director"


def apply_discount(price: float, pct: float) -> float:
    """Return the laptop price after applying a discount."""
    return price * (1 - pct / 100)
