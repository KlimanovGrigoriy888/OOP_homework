from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для описания продукта"""

    name: str  # Название продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество в наличии

    # Словарь для хранения имен добавленных продуктов с последними значениями цен и количества
    added_name_products: dict  # Анотация типа словаря
    added_name_products = {}  # Создание пустого словаря

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        # Проверка создания нового продукта на количество, если количество равно нулю возникает исключение
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    # Магический метод для вывода информации об объекте класса продукта.
    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    # Класс метод добавления продукта, вызов метода через атрибут класса.
    @classmethod
    def new_product(cls, new_product: dict):
        product = cls(
            name=new_product.get("name"),
            description=new_product.get("description"),
            price=new_product.get("price", 0.0),
            quantity=new_product.get("quantity", 0),
        )
        if product.name in Product.added_name_products:
            #  добавление количества продукта если он уже имеется в словаре имен продуктов с количеством и ценой
            Product.added_name_products[product.name][0] += new_product.get("quantity", 0)
            #  Условие если товар уже имеется в словаре имен продуктов с количеством и ценой, но цена выше старой
            if new_product.get("price", 0.0) > Product.added_name_products[product.name][1]:
                Product.added_name_products[product.name][1] = new_product.get("price", 0.0)
            #  Условие если товар уже имеется в словаре имен продуктов с количеством и ценой, но цена ниже старой
            else:
                pass
        #  добавление количества продукта если он не имеется в словаре имен продуктов с количеством и ценой
        else:
            Product.added_name_products[product.name] = [new_product.get("quantity", 0), new_product.get("price", 0.0)]
        return product

    # Метод геттер для вывода данных приватного атрибута цены
    @property
    def price(self) -> float:
        return self.__price

    # Setter для установки атрибуту price нового значения цены
    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price <= Product.added_name_products[self.name][1]:
            result = input(
                f"Цена товара {self.name} понижается, введите 'y' если согласны поменять цену, если нет введите 'n'\n="
            )
            if result == "y":
                self.__price = new_price
                Product.added_name_products[self.name][1] = new_price
            elif result == "n":
                pass  # Ничего не делаем, цена остаётся прежней
        elif new_price > Product.added_name_products[self.name][1]:
            self.__price = new_price
            Product.added_name_products[self.name][1] = new_price

    def __add__(self, other) -> float:
        """Магический метод для сложения суммарной стоимости продукта с суммарной стоимостью другого продукта"""
        if type(other) is Product:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Возникла ошибка TypeError при попытке сложения")


# if __name__ == "__main__":
#
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

# print(product1.name)
# print(product1.description)
# print(product1.price)
# print(product1.quantity)
#
# print(product2.name)
# print(product2.description)
# print(product2.price)
# print(product2.quantity)
#
# print(product3.name)
# print(product3.description)
# print(product3.price)
# print(product3.quantity)
