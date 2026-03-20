import pytest

from src.product import Product
from unittest.mock import patch


def test_product():
    # Очищаем словарь, чтобы тесты были независимыми
    Product.added_name_products = {}

    # Тест для проверки добавления нового продукта product_0
    product_0 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 18000.0,
            "quantity": 5,
        }
    )
    assert product_0.quantity == 5
    assert product_0.price == 18000.0

    # Тест вывода информации о продукте

    assert str(product_0) == "Samsung Galaxy S23 Ultra, 18000.0 руб. Остаток: 5 шт."

    # Тест для проверки добавления нового продукта product_1
    product_1 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 18000.0,
            "quantity": 5,
        }
    )
    assert product_1.quantity == 5
    assert product_1.price == 18000.0

    # Проверка состояния атрибута класса в виде словаря который хранит данные имени и цене товаров.
    assert Product.added_name_products == {"Samsung Galaxy S23 Ultra": [10, 18000.0]}

    # Тест сложения суммарной стоимости продукта
    result = product_0 + product_1
    assert result == 180000

    # Тест сеттера

    # 1. Повышение цены (проходит без input)
    product_1.price = 200000.0
    assert product_1.price == 200000.0

    # 2. Снижение цены — СОГЛАСИЕ (имитируем ввод 'y')
    with patch("builtins.input", return_value="y"):
        product_1.price = 150000.0
        assert product_1.price == 150000.0

    # 3. Снижение цены — ОТКАЗ (имитируем ввод 'n')
    with patch("builtins.input", return_value="n"):
        product_1.price = 100000.0
        # Цена должна остаться 150000.0, так как мы нажали 'n'
        assert product_1.price == 150000.0

    # 4. Некорректная цена
    product_1.price = -100
    assert product_1.price == 150000.0

def test_product_assert():
   # Тест на исключение добавления продукта с нулевым количеством
   with pytest.raises(ValueError):
    product_2 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "456GB, Белый цвет, 200MP камера",
            "price": 18000.0,
            "quantity": 0,
        }
    )
