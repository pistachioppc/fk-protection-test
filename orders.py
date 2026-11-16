def total(amounts):
    return sum(amounts)


def total_with_vat(amounts, rate=0.255):
    return round(total(amounts) * (1 + rate), 2)
