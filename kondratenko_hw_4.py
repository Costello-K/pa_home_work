import math


# 1. Є дев'ятиповерховий будинок, в якому 4 під'їзди. Номер під'їзду починається з одиниці.
# На одному поверсі - 4 квартири. Напишіть програму, яка від користувача отримує номер
# квартири та виводить для заданої квартири номер під'їзду, поверху та номер на поверсі.
# Якщо такої квартири немає в цьому будинку, то необхідно повідомити користувача про це.

number = int(input('Enter number'))
print(f'Entrance - {math.ceil(number / 36)}\n'
      f'Floor - {math.ceil(number % 36 / 4) or 9}\n'
      f'Apartment - {number % 4 or 4}')

# 2. Написати програму, яка буде повертати для заданого року кількість днів. Рік є
# високосним, якщо він кратний 4, але не кратний 100, а також якщо він кратний 400

# version 1

year = int(input('Enter year'))
if not year % 400:
    print("There are 366 days in the selected year")
elif not year % 100:
    print('There are 365 days in the selected year')
elif not year % 4:
    print('There are 366 days in the selected year')
else:
    print('There are 365 days in the selected year')

# version 2

days = 365
if not year % 400:
    days = 366
elif not year % 100:
    pass
elif not year % 4:
    days = 366
print(f'There are {days} days in the selected year')

# 3. Трикутник існує лише тоді, коли сума будь-яких двох сторін більше третьої.
# Дано: A, B, C - сторони трикутника. Напишіть програму, яка вказує чи існує такий трикутник.

a, b, c = 1, 5, 6
if a + b > c and b + c > a and c + a > b:
    p = (a + b + c) / 2
    area_triangle = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f'{area_triangle:.2f}')
else:
    print('Error. The sum of any two sides of a triangle must be greater than the third')
