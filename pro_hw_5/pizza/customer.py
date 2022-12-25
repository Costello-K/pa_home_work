class Customer:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def __str__(self):
        raise NotImplementedError


class CustomerWithHomeDelivery(Customer):
    def __init__(self, name, surname, telephone):
        super().__init__(name, surname)
        self.telephone = telephone

    def __str__(self):
        return f'{self._name} {self._surname}. Telephone: {self.telephone}'


class CustomerInPizzeria(Customer):
    def __init__(self, name, surname, table):
        super().__init__(name, surname)
        self.table = table

    def __str__(self):
        return f'{self._name} {self._surname}. Table: {self.table}'
