class Human:
    """

    """

    def __init__(self, name: str, surname: str, date_birth: str):
        """
        :param name: student's name
        :param surname: student's surname
        :param date_birth: date of birth
        """
        self.name = name
        self.surname = surname
        self.date_birth = date_birth

    def __str__(self):
        return f'{self.name} {self.surname}, date of birth: {self.name}'
