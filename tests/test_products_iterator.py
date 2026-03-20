from src.products_iterator import ProductIterator


# Тест для класса ProductIterator, проверка продуктов в экземпляре класса.
def test_products_iterator(category_first_category):
    products = ["Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.", "Iphone 15, 210000.0 руб. Остаток: 8 шт."]
    product_list = ProductIterator(category_first_category)
    for i, product in enumerate(product_list):
        # print(products[i])
        assert str(product) == products[i]
        assert str(product) == products[i]
