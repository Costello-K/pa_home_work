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
