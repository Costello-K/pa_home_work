import math


# 1. Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці.
# На одному поверсі - 4 квартири. Напишіть програму, яка від користувача отримує номер
# квартири та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі.
# Якщо такої квартири немає в цьому будинку, то необхідно повідомити користувача про це.

number = int(input('Enter number'))
FLOORS = 9
FLATS_IN_FLOOR = 4
FLATS_IN_ENTRANCE = FLATS_IN_FLOOR * FLOORS

print(f'Entrance - {math.ceil(number / FLATS_IN_ENTRANCE)}\n'
      f'Floor - {math.ceil(number % FLATS_IN_ENTRANCE / FLATS_IN_FLOOR) or FLOORS}\n'
      f'Apartment - {number % FLATS_IN_FLOOR or FLATS_IN_FLOOR}')

# 2. Написати програму, яка буде повертати для заданого року кількість днів. Рік є
# високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400

year = int(input('Enter year'))
days = 366 if year % 100 and not year % 4 or not year % 400 else 365
print(f'There are {days} days in the selected year')

# 3. Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої.
# Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує такий трикутник.

a, b, c = int(input('Enter side "a"')),\
          int(input('Enter side "b"')),\
          int(input('Enter side "c"'))
if a + b > c and b + c > a and c + a > b:
    p = (a + b + c) / 2
    area_triangle = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'{area_triangle:.2f}')
else:
    print('Error. The sum of any two sides of a triangle must be greater than the third')
