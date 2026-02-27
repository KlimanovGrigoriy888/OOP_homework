
def test_first_product(products_first):
    assert products_first.name == "Samsung Galaxy S23 Ultra"
    assert products_first.description == "256GB, Серый цвет, 200MP камера"
    assert products_first.quantity == 5
    assert products_first.price == 180000.0
