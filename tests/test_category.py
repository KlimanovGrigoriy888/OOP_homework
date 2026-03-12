from src.сategory import Category
from src.product import Product


def test_category_second_category(category_first_category, category_second_category):
    # Проверка создания атрибутов класса Category
    assert category_first_category.name == "Смартфоны"
    assert category_second_category.name == "Телевизоры"
    assert (
        category_first_category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert (
        category_second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_first_category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт." "\nIphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert category_first_category.category_count == 2
    assert category_first_category.product_count == 3
    assert category_second_category.name == "Телевизоры"
    assert (
        category_second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_second_category.products == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n'
    assert category_second_category.category_count == 2
    assert category_second_category.product_count == 3

    # Создание нового продукта через класс Product и добавление этого продукта через метод атрибута класса Category
    product2 = Product('32" QLED 4K', "Фоновая подсветка", 60000.0, 2)
    category_second_category.add_product(product2)

    # Проверка добавление продукта через метод атрибута класса Category
    assert (
        category_second_category.products
        == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.\n32" QLED 4K, 60000.0 руб. Остаток: 2 шт.\n'
    )
    assert category_second_category.name == "Телевизоры"
    assert (
        category_second_category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert Category.category_count == 2
    assert Category.product_count == 4

    # Проверка вывода информации о категории
    assert str(category_first_category) == "Смартфоны, количество продуктов: 13 шт."
