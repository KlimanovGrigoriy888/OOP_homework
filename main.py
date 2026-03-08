from src.product import Product
from src.products_iterator import ProductIterator
from src.сategory import Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                             "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                             [product4])
    product5 = Product("32\" QLED 4K", "Фоновая подсветка", 60000.0, 2)
    category2.add_product(product5)

    print("////////")
    print(str(category1))
    print(str(category2))
    print(category1.products)
    print(category1.products_list)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
    product_list = ProductIterator(category1)
    next(iter(product_list))
    next(iter(product_list))
    # product_iter = ProductIterator(category1)
    # for product in product_iter:
    #     print(product)


    # #Старые проверки №2
    # product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    # product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    # product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    #
    # category1 = Category(
    #     "Смартфоны",
    #     "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    #     [product1, product2, product3],
    # )
    #
    # print(category1.products)
    # product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    # category1.add_product(product4)
    # print(category1.products)
    # print(category1.product_count)
    #
    # new_product = Product.new_product(
    #     {
    #         "name": "Samsung Galaxy S23 Ultra",
    #         "description": "256GB, Серый цвет, 200MP камера",
    #         "price": 180000.0,
    #         "quantity": 5,
    #     }
    # )
    # print(new_product.name)
    # print(new_product.description)
    # print(new_product.price)
    # print(new_product.quantity)
    #
    # new_product.price = 800
    # print(new_product.price)
    #
    # new_product.price = -100
    # print(new_product.price)
    # new_product.price = 0
    # print(new_product.price)

# #Старые проверки №1
# if __name__ == "__main__":
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 2)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.quantity)
#
#     print(product3.name)
#     print(product3.description)
#     print(product3.quantity)
#
#     product4 = Product.new_product(
#         {"name": "Samsung Galaxy S23 Ultra",
#          "description": "256GB, Серый цвет,"
#          " 200MP камера", "price": 18000.0,
#          "quantity": 10})
#     print(product1.name)
#     print(product1.description)
#     print(product1.quantity)
#     product1.price = 4000
#     print(product1.price)
#     print(Product.added_name_products)
#
#     category1 = Category("Смартфоны",
#                          "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#                          [product1, product2, product3])
#
#     print(category1.name == "Смартфоны")
#     print(category1.description)
#     print(category1.category_count)
#     print(category1.product_count)
#
#     product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
#     category2 = Category("Телевизоры",
#                          "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
#                          [product4])
#     print("////////")
#     print(category2.name)
#     print(category2.description)
#     print(Category.category_count)
#     print(Category.product_count)
#     print("///////")
#     product5 = Product("32\" QLED 4K", "Фоновая подсветка", 60000.0, 2)
#     category2.add_product(product5)
#     print(category2.name)
#     print(category2.description)
#     print(Category.category_count)
#     print(Category.product_count)
#     print(category1.products)
#     print(category2.products)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [
#             Product("Samsung Galaxy S23 Ultra", "256GB," " Серый цвет, 200MP камера", 180000.0, 5),
#             Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
#         ],
#     )
#
#     print(category1.products)
