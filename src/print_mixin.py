class PrintMixin:
    """Класс типа mixin для вывода информации при создании нового объекта класса если объявлен в классе наследнике
    в формате "Название класса, (название продукта, описание продукта, цена, количество)"."""

    def __init__(self) -> None:
        # Вызывает метод __repr__ при инициализации класса Product так как класс PrintMixin является дочерним классом
        # mixin для класса Product в котором имеет вызов через super().__init__
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"
