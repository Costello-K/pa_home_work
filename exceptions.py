class InvalidArgument(Exception):
    """Exception raised for invalid value"""

    def __init__(self, message):
        """
        :param message: explanation of the error
        """
        super().__init__()
        self.message = message

    def __str__(self):
        return f'InvalidValue: {self.message}'


class ExceedingTheLimit(InvalidArgument):
    """Exception raised for value is greater than limit"""

    def __init__(self, message):
        """
        :param message: explanation of the error
        """
        super().__init__(message)

    def __str__(self):
        return f'ExceedingTheLimit: {self.message}'
