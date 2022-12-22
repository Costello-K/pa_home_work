from modules import save_result_to_file


class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @save_result_to_file
    def __str__(self):
        return f'{self.name} {self.surname}'
