class Deliveryman:
    def __init__(self, name, surname, telephone):
        self.__name = name
        self.__surname = surname
        self.__telephone = telephone

    def __str__(self):
        return f'{self.__name} {self.__surname}: {self.__telephone}'
