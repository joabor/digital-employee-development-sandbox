from __future__ import annotations


def calculate_reference_value(base_amount: float, adjustment_percent: float) -> float:
    """Return the adjusted reference value rounded to two decimals.

    The public contract for edge cases is documented in README.md.
    """
    return round(base_amount * (1 + adjustment_percent / 100), 2)
