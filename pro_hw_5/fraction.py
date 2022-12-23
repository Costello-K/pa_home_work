from math import gcd
from decimal import Decimal


class Fraction:
    """
    Proper or improper fractions.
    Supports comparison, multiplication, addition, subtraction operations of instances of this class
    """
    def __init__(self, numerator: int, denominator: int):
        """
        :param numerator: top number in fraction
        :param denominator: bottom number in fraction
        """
        if not isinstance(numerator, int) and not isinstance(denominator, int):
            raise TypeError('Parameters must be only Integer')
        if not denominator:
            raise ZeroDivisionError('Denominator cannot be 0')
        self.__numerator = numerator < 0 < denominator and numerator \
            or numerator > 0 > denominator and -numerator or abs(numerator)
        self.__denominator = abs(denominator)
        self.__is_divisor()

    def __str__(self):
        return f'Fraction: {self.__numerator}/{self.__denominator}'

    def __gt__(self, other):
        self.__is_class_exemplar(other)
        return self.float_number() > other.float_number()

    def __lt__(self, other):
        self.__is_class_exemplar(other)
        return self.float_number() < other.float_number()

    def __ge__(self, other):
        self.__is_class_exemplar(other)
        return self.float_number() >= other.float_number()

    def __le__(self, other):
        self.__is_class_exemplar(other)
        return self.float_number() <= other.float_number()

    def __eq__(self, other):
        self.__is_class_exemplar(other)
        return self.float_number() == other.float_number()

    def __ne__(self, other):
        self.__is_class_exemplar(other)
        return self.float_number() != other.float_number()

    def __add__(self, other):
        self.__is_class_exemplar(other)
        denominator = self.__compound_denominator(other.__denominator)
        numerator = self.__addition(other, denominator)
        return Fraction(numerator, denominator)

    def __iadd__(self, other):
        self.__is_class_exemplar(other)
        denominator = self.__compound_denominator(other.__denominator)
        self.__numerator = self.__addition(other, denominator)
        self.__denominator = denominator
        return self

    def __sub__(self, other):
        self.__is_class_exemplar(other)
        denominator = self.__compound_denominator(other.__denominator)
        numerator = self.__subtraction(other, denominator)
        return Fraction(numerator, denominator)

    def __isub__(self, other):
        self.__is_class_exemplar(other)
        denominator = self.__compound_denominator(other.__denominator)
        self.__numerator = self.__subtraction(other, denominator)
        self.__denominator = denominator
        self.__is_divisor()
        return self

    def __mul__(self, other):
        self.__is_class_exemplar(other)
        return Fraction(self.__numerator * other.__numerator, self.__denominator * other.__denominator)

    def __imul__(self, other):
        self.__is_class_exemplar(other)
        self.__numerator *= other.__numerator
        self.__denominator *= other.__denominator
        self.__is_divisor()
        return self

    def __is_class_exemplar(self, exemplar):
        if not isinstance(exemplar, Fraction):
            raise TypeError(f'"{exemplar}" is not an instance of class ProperFraction')

    def __compound_denominator(self, denominator):
        return self.__denominator * denominator // gcd(self.__denominator, denominator)

    def float_number(self):
        # return round(self.numerator / self.denominator, 9)
        return Decimal(self.__numerator / self.__denominator).quantize(Decimal("1.000000000"))

    def __is_divisor(self):
        divisor = gcd(self.__numerator, self.__denominator)
        if divisor > 1:
            self.__numerator //= divisor
            self.__denominator //= divisor

    def __addition(self, other, denominator):
        return denominator // self.__denominator * self.__numerator \
               + denominator // other.__denominator * other.__numerator

    def __subtraction(self, other, denominator):
        return denominator // self.__denominator * self.__numerator \
               - denominator // other.__denominator * other.__numerator
