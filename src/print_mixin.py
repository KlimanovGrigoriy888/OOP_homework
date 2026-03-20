class PrintMixin:
    """Класс типа mixin для вывода информации при создании нового объекта класса если объявлен в классе наследнике
    в формате "Название класса, (название продукта, описание продукта, цена, количество)"."""

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} ({self.name}, {self.description}, {self.price}, {self.quantity})"
