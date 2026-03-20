from src.сategory import Category


class ProductIterator:
    """Класс принимает экземпляр класса категории продукта и возвращает итератор для перебора класса продуктов
    из класса категории продукта"""

    category: Category  # экземпляр класса категории товаров, указываем класс.

    # Инициализация атрибута класса, которым является экземпляр класса категории продукта.
    def __init__(self, category):
        self.category = category if category else None

    # Магический метод вызывающий итератор со стартом с 0 значения.
    def __iter__(self):
        self.index_value = -1
        return self

    # Магический метод создает следующий шаг итерации с проверкой завершения итератора по длине списка продуктов
    # в классе категории товара.
    def __next__(self):
        if self.index_value + 1 < len(self.category.products_list):
            self.index_value += 1  # итерация от 0 до длины списка продуктов.
            return self.category.products_list[self.index_value]
        else:
            raise StopIteration
