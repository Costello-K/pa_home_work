from rectangle import Rectangle
from fraction import Fraction


if __name__ == '__main__':
    rectangle_1 = Rectangle(4, 6)
    rectangle_2 = Rectangle(10, 9)
    rectangle_3 = 2 * Rectangle(10, 9) * 2
    rectangle_4 = (10, 9)
    summa = [10, 9] + rectangle_1 + rectangle_2 + rectangle_3 + rectangle_4
    print(rectangle_1 == rectangle_2)
    print(rectangle_2 == rectangle_3)
    print(rectangle_1, rectangle_2, rectangle_3, rectangle_4, summa, sep='\n')

    t1 = Fraction(1, 2)
    t2 = Fraction(1, 2)
    t3 = Fraction(-6, 8)
    t4 = Fraction(10, -12)
    t5 = Fraction(-10, -11)
    t6 = Fraction(0, -11)
    print(t1, t2, t3, t4, t5, t6, sep='\n')
    t1 *= t2
    print(t1)
