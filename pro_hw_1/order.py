from exceptions import InvalidArgument
from product import Product
from customer import Customer
from order_iterator import OrderIterator


class Order:
    """
    Shopping cart
    Supports methods for adding products
    """
    __order = 0

    def __init__(self, customer: Customer):
        """
        :param customer: an instance of the class Customer
        """
        Order.__order += 1
        self.__order_number = Order.__order
        self.__products = {}
        if not isinstance(customer, Customer):
            raise InvalidArgument(f'"{customer}" is not an instance of a class Customer')
        self.customer = customer

    def __str__(self):
        return f'Order {self.__order_number}:\n{str(self.customer)}\n' + \
               '\n'.join(f'{i} - {self.__products[i]["amount"]}' for i in self.__products.keys()) + \
               f'\nTotal price: {self.get_price()}'

    def __iter__(self):
        return OrderIterator(self.__products.keys())

    def __len__(self):
        return self.__products.__len__()

    def __getitem__(self, name):
        return self.__products[name]

    def items(self):
        return iter(self.__products.items())

    def keys(self):
        return iter(self.__products.keys())

    def values(self):
        return iter(self.__products.values())

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise InvalidArgument(f'"{product}" is not an instance of a class Product')
        if self.__products.get(product.title):
            self.__products[product.title]['amount'] += 1
        else:
            self.__products[product.title] = {'amount': 1, 'price': product.price}

    def get_price(self):
        return sum(map(lambda i: i['price'] * i['amount'], self.__products.values()))
