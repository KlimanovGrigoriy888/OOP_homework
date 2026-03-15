from src.product import Product


class Smartphone(Product):
    """Класс Smartphone наследник от класса Product для создания продуктов типа смартфон с расширенными атрибутами:
    efficiency- Производительность, model - Модель, memory - Объем встроенной памяти, color - Цвет."""

    name: str  # Название продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество в наличии
    efficiency: float  # Производительность, новый атрибут класса Smartphone
    model: str  # Модель, новый атрибут класса Smartphone
    memory: int  # Объем встроенной памяти, новый атрибут класса Smartphone
    color: str  # Цвет, новый атрибут класса Smartphone

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    )  -> None:
        #  Функция которая, вызывает методы и атрибуты родительского класса
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Магический метод для сложения суммарной стоимости продукта с суммарной стоимостью другого продукта"""
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Возникла ошибка TypeError при попытке сложения")

if __name__ == "__main__":
    print(Smartphone.__mro__)