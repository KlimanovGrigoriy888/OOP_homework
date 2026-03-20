class ZeroPriceAddProduct(Exception):  # Новый класс исключения
    def __init__(self, message):
        super().__init__(message)
