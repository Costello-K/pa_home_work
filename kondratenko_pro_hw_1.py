from product import Product
from customer import Customer
from order import Order


product_apple = Product('apple', 10.00, 'fruit')
product_orange = Product('orange', 50.059, 'fruit')

customer_1 = Customer('Ivan', 'Ivanov', '+380635556644')
customer_2 = Customer('Petro', 'Petrov', '+380639596949')

order_1, order_2 = Order(customer_2), Order(customer_1)

order_1.add_product(product_apple)
order_1.add_product(product_orange)
order_1.add_product(product_apple)

order_2.add_product(product_apple)
order_2.add_product(product_apple)
order_2.add_product(product_apple)

print(order_1, order_2, sep='\n')










