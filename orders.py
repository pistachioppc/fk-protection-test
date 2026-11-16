"""Toy order totals for the protection test."""


def total(amounts):
    return sum(amounts)


def total_with_vat(amounts, rate=0.255):
    return round(total(amounts) * (1 + rate), 2)


def total_with_discount(amounts, percent):
    if percent > 100:
        raise ValueError("discount above 100 %")
    return round(total(amounts) * (1 - percent), 2)
