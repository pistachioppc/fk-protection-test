from orders import total


def test_total():
    assert total([1, 2]) == 3


def test_empty():
    assert total([]) == 0


def test_vat():
    from orders import total_with_vat

    assert total_with_vat([100]) == 125.5
    assert total_with_vat([]) == 0
