import pytest

from src.lawngrass import LawnGrass


def test_init_lawngrass(lawngrass_new_1, lawngrass_new_2):
    assert lawngrass_new_1.name == "Газонная трава"
    assert lawngrass_new_1.description == "Элитная трава для газона"
    assert lawngrass_new_1.price == 500.0
    assert lawngrass_new_1.quantity == 20
    assert lawngrass_new_1.country == "Россия"
    assert lawngrass_new_1.germination_period == "7 дней"
    assert lawngrass_new_1.color == "Зеленый"

    assert lawngrass_new_2.name == "Газонная трава 2"
    assert lawngrass_new_2.description == "Выносливая трава"
    assert lawngrass_new_2.price == 450.0
    assert lawngrass_new_2.quantity == 15
    assert lawngrass_new_2.country == "США"
    assert lawngrass_new_2.germination_period == "5 дней"
    assert lawngrass_new_2.color == "Темно-зеленый"


def test_add_lawngrass(lawngrass_new_1, lawngrass_new_2):
    assert lawngrass_new_1 + lawngrass_new_2 == 16750.0


def test_add_lawngrass_error(lawngrass_new_1, smartphone_new_1):
    with pytest.raises(TypeError):
        lawngrass_new_1 + smartphone_new_1


def test_add_lawngrass_assert():
    # Тест на исключение добавления продукта с нулевым количеством
    with pytest.raises(ValueError):
        LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 0, "Россия", "7 дней", "Зеленый")
