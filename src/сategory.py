from src.product import Product


class Category:
    """Класс для описания категории продукта"""

    name: str  # Название категории продукта
    description: str  # Описание категории продукта
    __products: list[Product]  # Список товаров категории Product

    category_count = 0  # Атрибуты класса счетчик категорий продукта
    product_count = 0  # Атрибуты класса счетчик добавленных продуктов класса Product

    # словарь добавленных категорий продукта для проверки дубликатов названий категорий для правильного подсчета
    # количества добавленных категорий продукта category_count
    added_category_products: dict[str, str]
    added_category_products = {}

    def __init__(self, name: str, description: str, products=None):
        # self.price = None
        self.name = name
        self.description = description
        self.__products = products if products else []  # приватный атрибут класса Category
        # Условие добавления счетчика категории продукта с проверкой дубликатов названия категории
        if name in Category.added_category_products:
            pass
        if name not in Category.added_category_products:
            Category.added_category_products[name] = name
            Category.category_count += 1
        # Счетчик атрибут класса для подсчета добавленных продуктов класса Product
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        # Подсчет общего количества продуктов в категории продукта
        # упростил код, оказывается функция sum() умеет делать next, тем самым распаковывать генераторное выражение
        full_quantity_products = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {full_quantity_products} шт."

    # Метод добавления продукта в приватный атрибут продукта категории продукта.
    def add_product(self, new_product: Product) -> None:
        #  Проверка добавленного продукта принадлежности к родительскому классу Product
        if isinstance(new_product, Product):
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
    def products_list(self) -> list:
        products_list = []
        for product in self.__products:
            products_list.append(str(product))
        return products_list

    # Метод подсчитывает средний ценник всех товаров категории продукта
    def middle_price(self):
        # Отлавливаем исключение ZeroDivisionError при условии если список продуктов категории пустой и возвращаем 0
        try:
            return round(sum(product.price for product in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
