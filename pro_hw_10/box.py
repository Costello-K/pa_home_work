# 3) Для класса Box напишите статический метод, который будет подсчитывать суммарный
# объем  двух ящиков, которые  будут его параметрами.
class Box:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def __setattr__(self, key, value):
        if key in ('width', 'length', 'height'):
            if not isinstance(value, int):
                raise TypeError
            if value <= 0:
                raise ValueError
            self.__dict__[key] = value

    def __str__(self):
        return f'Box: {self.width} x {self.length} x {self.height}'

    def volume(self):
        return self.width * self.length * self.height

    @staticmethod
    def sum_volume(*args):
        if not all(isinstance(i, Box) for i in args):
            raise TypeError
        return sum(box.volume() for box in args)

    # @staticmethod
    # def sum_volume(*args):
    #     if not all(isinstance(i, Box) for i in args):
    #         raise TypeError
    #     return sum(box.height * box.width * box.length for box in args)
