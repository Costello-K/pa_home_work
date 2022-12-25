from decimal import Decimal


class Rectangle:
    """
    Figure rectangle.
    Supports methods for comparing rectangles by area, adding rectangles, multiplying by a number
    """
    def __init__(self, a: int | float | Decimal, b: int | float | Decimal):
        """
        :param a: rectangle length
        :param b: rectangle width
        """
        if not isinstance(a, int | float | Decimal) and not isinstance(b, int | float | Decimal):
            raise TypeError('Parameters must be only Integer, Float or Decimal')
        if Decimal(a).quantize(Decimal("1.000")) <= 0 or Decimal(b).quantize(Decimal("1.000")) <= 0:
            raise ValueError('Parameters must be greater than 0')
        self.a = Decimal(a).quantize(Decimal("1.000"))
        self.b = Decimal(b).quantize(Decimal("1.000"))

    def __str__(self):
        return f'Rectangle: a = {self.a}, b = {self.b}, S = {self.area()}, P = {self.perimeter()}'

    def __gt__(self, other):
        self.__is_class_exemplar(other)
        return self.area() > other.area()

    def __lt__(self, other):
        self.__is_class_exemplar(other)
        return self.area() < other.area()

    def __ge__(self, other):
        self.__is_class_exemplar(other)
        return self.area() >= other.area()

    def __le__(self, other):
        self.__is_class_exemplar(other)
        return self.area() <= other.area()

    def __eq__(self, other):
        self.__is_class_exemplar(other)
        return self.area() == other.area()

    def __ne__(self, other):
        self.__is_class_exemplar(other)
        return self.area() != other.area()

    def __add__(self, other):
        if self.__addition(other):
            return self.__addition(other)
        return NotImplemented

    def __radd__(self, other):
        if self.__addition(other):
            return self.__addition(other)
        raise TypeError('Invalid argument data type')

    def __iadd__(self, other):
        a = max(self.a, self.b)
        if isinstance(other, Rectangle):
            self.a = a
            self.b = (self.area() + other.area()) / a
            return self
        if isinstance(other, list | tuple) and len(other) == len(self.__dict__):
            sub_a, sub_b = other
            if isinstance(sub_a, int | float | Decimal) and isinstance(sub_b, int | float | Decimal):
                self.a = a
                self.b = (self.area() + Rectangle(sub_a, sub_b).area()) / a
                return self
            raise TypeError('Wrong data type in sequence')
        raise TypeError('Invalid argument data type')

    def __mul__(self, other: int | float | Decimal):
        if isinstance(other, int | float | Decimal):
            return self.__multiplication(other)
        return NotImplemented

    def __rmul__(self, other: int | float | Decimal):
        if isinstance(other, int | float | Decimal):
            return self.__multiplication(other)
        raise TypeError('Invalid argument data type')

    def __imul__(self, other: int | float | Decimal):
        if isinstance(other, int | float | Decimal):
            return self.__multiplication(other)
        raise TypeError('Invalid argument data type')

    def area(self):
        return (self.a * self.b).quantize(Decimal("1.000"))

    def perimeter(self):
        return (self.a + self.b) * 2

    @staticmethod
    def __is_class_exemplar(exemplar):
        if not isinstance(exemplar, Rectangle):
            raise TypeError(f'"{exemplar}" is not an instance of class Rectangle')

    def __addition(self, other):
        a = max(self.a, self.b)
        if isinstance(other, Rectangle):
            return Rectangle(a, (self.area() + other.area()) / a)
        if isinstance(other, list | tuple) and len(other) == len(self.__dict__):
            sub_a, sub_b = other
            if isinstance(sub_a, int | float | Decimal) and isinstance(sub_b, int | float | Decimal):
                return Rectangle(a, (self.area() + Rectangle(sub_a, sub_b).area()) / a)
            raise TypeError('Wrong data type in sequence')
        raise TypeError('Wrong var')

    def __multiplication(self, other):
        n = Decimal(other).sqrt()
        self.a = (self.a * n).quantize(Decimal("1.000"))
        self.b = (self.b * n).quantize(Decimal("1.000"))
        return self

