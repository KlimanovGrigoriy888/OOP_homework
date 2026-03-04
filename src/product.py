class Product:
    """Класс для описания продукта"""

    name: str  # Название продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество в наличии

    added_name_products = {}

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    # Класс метод добавления продукта
    @classmethod
    def new_product(cls, new_product: dict):
        product = cls(
            name=new_product.get("name"),
            description=new_product.get("description"),
            price=new_product.get("price", 0.0),
            quantity=new_product.get("quantity", 0),
        )
        if product.name in Product.added_name_products:
            Product.added_name_products[product.name][0] += new_product.get("quantity", 0)
            if new_product.get("price", 0.0) > Product.added_name_products[product.name][1]:
                Product.added_name_products[product.name][1] = new_product.get("price", 0.0)
            else:
                pass
        else:
            Product.added_name_products[product.name] = [new_product.get("quantity", 0), new_product.get("price", 0.0)]
        return product

    # Метод геттер для вывода данных приватного атрибута цены
    @property
    def price(self):
        return self.__price

    # Setter для установки атрибуту цена нового значения цены
    @price.setter
    def price(self, new_price: float):
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
