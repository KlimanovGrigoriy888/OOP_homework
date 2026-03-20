import pytest

from src.smartphone import Smartphone


def test_init_smartphone(smartphone_new_1, smartphone_new_2):
    assert smartphone_new_1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_new_1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_new_1.price == 180000.0
    assert smartphone_new_1.quantity == 5
    assert smartphone_new_1.efficiency == 95.5
    assert smartphone_new_1.model == "S23 Ultra"
    assert smartphone_new_1.memory == 256
    assert smartphone_new_1.color == "Серый"

    assert smartphone_new_2.name == "Iphone 15"
    assert smartphone_new_2.description == "512GB, Gray space"
    assert smartphone_new_2.price == 210000.0
    assert smartphone_new_2.quantity == 8
    assert smartphone_new_2.efficiency == 98.2
    assert smartphone_new_2.model == "15"
    assert smartphone_new_2.memory == 512
    assert smartphone_new_2.color == "Gray space"


def test_add_smarphone(smartphone_new_1, smartphone_new_2):
    assert smartphone_new_1 + smartphone_new_2 == 2580000


def test_add_smartphone_error(smartphone_new_1, lawngrass_new_1):
    with pytest.raises(TypeError):
        smartphone_new_1 + lawngrass_new_1


def test_add_smartphone_assert():
    # Тест на исключение добавления продукта с нулевым количеством
    with pytest.raises(ValueError):
        Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 0, 90.3, "Note 11", 1024, "Синий")
