class OrderIterator:
    def __init__(self, data_products):
        self.data_products = tuple(data_products)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data_products):
            self.index += 1
            return self.data_products[self.index - 1]
        raise StopIteration
