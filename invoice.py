from decimal import Decimal, ROUND_HALF_UP

def invoice_total(lines: list[tuple[str, int]]) -> str:
    """Return currency total; round each extended line HALF_UP to cents."""
    total = Decimal("0.00")
    for price, quantity in lines:
        amount = Decimal(price) * Decimal(quantity)
        rounded_amount = amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        total += rounded_amount
    return f"{total:.2f}"
