class Waiter:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def __str__(self):
        return f'{self.__name} {self.__surname}'
