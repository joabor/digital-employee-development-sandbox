"""Synthetic invoice totals, independent of the platform."""


def invoice_total(lines: list[tuple[str, int]]) -> str:
    """Return currency total; round each extended line HALF_UP to cents."""
    return f"{round(sum(float(price) * quantity for price, quantity in lines), 2):.2f}"
