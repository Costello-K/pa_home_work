from human import Human


class Student(Human):
    """

    """

    def __init__(self, name: str, surname: str, date_birth: str, passport: str):
        """
        :param name: student's name
        :param surname: student's surname
        :param date_birth: date of birth
        :param passport: student passport number
        """
        super().__init__(name, surname, date_birth)
        self.passport = passport

    def __str__(self):
        return f'{self.name} {self.surname}. Passport: {self.passport}'
