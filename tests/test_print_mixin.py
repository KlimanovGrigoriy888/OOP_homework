from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_print_mixin_product(capsys):
    # Очищаем словарь, чтобы тесты были независимыми
    Product.added_name_products = {}
    product_1 = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 18000.0,
            "quantity": 5,
        }
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Product (Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 18000.0, 5)"
    assert product_1.name == "Samsung Galaxy S23 Ultra"


def test_print_mixin_smartphone(capsys):
    smartphone_new_1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone (Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    assert smartphone_new_1.name == "Samsung Galaxy S23 Ultra"


def test_print_mixin_lawngrass(capsys):
    lawngrass_new_1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    message = capsys.readouterr()
    assert message.out.strip() == "LawnGrass (Газонная трава, Элитная трава для газона, 500.0, 20)"
    assert lawngrass_new_1.name == "Газонная трава"
