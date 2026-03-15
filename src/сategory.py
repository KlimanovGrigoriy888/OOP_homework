from src.product import Product


class Category:
    """Класс для описания категории продукта"""

    name: str  # Название категории продукта
    description: str  # Описание категории продукта
    __products: list  # Список товаров категории
    category_count = 0  # Атрибуты класса счетчик категорий продукта
    product_count = 0  # Атрибуты класса счетчик классов добавленных продуктов

    added_category_products: dict[str]
    added_category_products = {}

    def __init__(self, name, description, products=None):
        self.price = None
        self.name = name
        self.description = description
        self.__products = products if products else []  # приватный атрибут класса Category
        # Условие добавления счетчика категории продукта с проверкой дубликатов названия категории
        if name in Category.added_category_products:
            pass
        if name not in Category.added_category_products:
            Category.added_category_products[name] = name
            Category.category_count += 1
        # Счетчик атрибут класса для подсчета классов добавленных продуктов
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        # Подсчет общего количества продуктов в категории продукта
        full_quantity_products = 0
        for product in self.__products:
            full_quantity_products += product.quantity
        return f"{self.name}, количество продуктов: {full_quantity_products} шт."

    # Метод добавления продукта в приватный атрибут продукта категории продукта.
    def add_product(self, new_product: Product):
        #  Проверка добавленного продукта принадлежности к родительскому классу Product
        if issubclass(new_product.__class__, Product):
            self.__products.append(new_product)
            Category.product_count += 1
        # Если не принадлежит родительскому классу, возникает исключение TypeError
        else:
            raise TypeError("Возникла ошибка TypeError при добавлении не продукта")

    # Метод 'getter' с помощью которого возможно посмотреть приватный атрибут продуктов
    @property
    def products(self):
        product_list = ""
        for product in self.__products:
            product_list += f"{str(product)}\n"
        return product_list

    # Метод getter экземпляра класса который создает список товаров для экземпляра класса категории продукта.
    @property
    def products_list(self):
        products_list = []
        for product in self.__products:
            products_list.append(str(product))
        return products_list
