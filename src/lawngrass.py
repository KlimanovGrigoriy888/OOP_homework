from src.product import Product


class LawnGrass(Product):
    """Класс LawnGrass наследник от класса Product для создания продуктов типа растение-трава с расширенными
    атрибутами: country - Страна, germination_period - Срок прорастания, color - Цвет."""

    name: str  # Название продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество в наличии
    country: str  # Страна, новый атрибут класса LawnGrass
    germination_period: str  # Срок прорастания, новый атрибут класса LawnGrass
    color: str  # Цвет, новый атрибут класса LawnGrass

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    )  -> None:
        #  Функция которая, вызывает методы и атрибуты родительского класса
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Магический метод для сложения суммарной стоимости продукта с суммарной стоимостью другого продукта"""
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError("Возникла ошибка TypeError при попытке сложения")
