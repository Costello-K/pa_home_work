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
