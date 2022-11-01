from exceptions import InvalidArgument


class Product:
    """

    """

    def __init__(self, title: str, price: int | float, description: str):
        """
        :param title: the product's name
        :param price: product price
        :param description: product description
        """
        self.title = title
        self.description = description
        if round(price, 2) <= 0:
            raise InvalidArgument('Price must be greater than zero')
        self.price = round(price, 2)

    def __str__(self):
        return '\n'.join(f'{k}: {v}' for k, v in self.__dict__.items())


class Customer:
    """

    """

    def __init__(self, name: str, surname: str, telephone: str):
        """
        :param name: customer name
        :param surname: customer surname
        :param telephone: customer telephone
        """
        self.name = name
        self.surname = surname
        self. telephone = telephone

    def __str__(self):
        return f'Customer: {self.name} {self.surname}, telephone: {self.telephone}'


class Order:
    """

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

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise InvalidArgument(f'"{product}" is not an instance of a class Product')
        if self.__products.get(product.title):
            self.__products[product.title]['amount'] += 1
        else:
            self.__products[product.title] = {'amount': 1, 'price': product.price}

    def get_price(self):
        return sum(map(lambda i: i['price'] * i['amount'], self.__products.values()))


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










