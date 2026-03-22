import pytest

from src.utils import read_json, make_objects_from_json
from unittest.mock import mock_open, patch

from src.сategory import Category


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1}]')
def test_read_json_valid(mock_open, mock_exists):
    mock_exists.return_value = True
    path = "test_path.json"
    result = read_json(path)
    assert result == [{"id": 1}]


@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data=None)
def test_read_json_not_data(mock_open, mock_exists):
    mock_exists.return_value = True
    path = "dummy_path.json"
    result = read_json(path)
    assert result == {}


@pytest.fixture
def list_products() -> list[dict]:
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            "products": [
                {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
            ],
        },
    ]


def test_make_objects_from_json_valid(list_products):
    Category.category_count = 0
    Category.product_count = 0

    product_category = make_objects_from_json(list_products)
    assert (
        product_category[0].description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert product_category[0].product_count == 3
    assert (
        product_category[0].products
        == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert product_category[0].name == "Смартфоны"
    assert product_category[1].product_count == 3
    assert (
        product_category[1].description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert product_category[1].products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
    assert product_category[1].name == "Телевизоры"
