import json
import os

from src.product import Product
from src.сategory import Category

PATH_TO_PRODUCTS_JSON = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")


def read_json(path: str) -> dict[list]:
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def make_objects_from_json(data: dict):
    """" Функция, принимает путь к файлу с категориями продуктов и продуктами,
     и создает объекты классов Category и Product"""
    category_product = []
    for category in data:
        products = []
        for product in category['products']:
            # В новый словарь создаем список продукта на основе класса Product продукта
            products.append(Product(**product))
        # В существующем списке категории продукта перезаписываем список списком класса Product
        category['products'] = products
        # В новый словарь категории продуктов добавляем категории продуктов на основе класса категории продукта
        category_product.append(Category(**category))

    return category_product


if __name__ == "__main__":
    data_products = read_json(PATH_TO_PRODUCTS_JSON)
    product_category = make_objects_from_json(data_products)

    print(product_category[0].description)
    print(product_category[0].product_count)
    print(product_category[0].products)
    print(product_category[0].name)
    print(product_category[1].product_count)
    print(product_category[1].description)
    print(product_category[1].products[0].name)
    print(product_category[1].name)