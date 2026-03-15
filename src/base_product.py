from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс который является родительским для классов продуктов, все наследуемые классы должны содержать
    инициализацию основных параметров продукта, и методы __str__- магический метод для вывода информации об объекте
    класса продукта и метод __add__ - сложения суммарной стоимости продукта с суммарной стоимостью другого продукта."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other):
        pass
