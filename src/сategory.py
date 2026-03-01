class Category:
    """Класс для описания категории продукта"""
    name: str  # Название категории продукта
    description: str  # Описание категории продукта
    products: list  # Список товаров категории
    category_count = 0  # Атрибуты класса счетчик категорий продукта
    product_count = 0  # Атрибуты класса счетчик всех продуктов

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0
