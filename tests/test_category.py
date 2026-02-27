

def test_category_first_category(category_first_category):
    assert category_first_category.name == "Смартфоны"
    assert category_first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category_first_category.products) == 2
    assert category_first_category.category_count == 1
    assert category_first_category.product_count == 2

def test_category_second_category(category_first_category, category_second_category):
    assert category_first_category.name == "Смартфоны"
    assert category_first_category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category_first_category.products) == 2
    assert category_first_category.category_count == 2
    assert category_first_category.product_count == 3
    assert category_second_category.name == "Телевизоры"
    assert category_second_category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    assert len(category_second_category.products) == 1
    assert category_second_category.category_count == 2
    assert category_second_category.product_count == 3