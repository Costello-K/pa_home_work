from random import randint

LINE_WIDTH = 50

# 1. Написати Python-скрипт, який виводить на екран усі числа в діапазоні від 1 до 100 кратні 7

num, divisor = int(input('Enter number')),\
               int(input('Enter divisor'))

if num < divisor:
    print(f'This range has no multiples of {divisor}')
else:
    print(f'{"numbers that are multiples of " + str(divisor):^{LINE_WIDTH}}'.upper())
    res = [print(i, end=', ') for i in range(divisor, num + 1, divisor)]
    print(f'\n{"end":^{LINE_WIDTH}}\n'.upper())

# 2. Написати Python-скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури)

num = int(input('Enter factorial'))

factorial = 1
for i in range(2, num + 1):
    factorial *= i
print(f'Factorial of a number "{num}" = {factorial}\n')

# 3. Написати Python-скрипт, який виводить на екран таблицю множення на 5
# Переважно друкувати 1 x 5 = 5, 2 x 5 = 10, а не просто 5, 10, ...

multiplier = int(input('Enter number from 1 to 9'))

for i in range(1, 11):
    print(f'{i} x {multiplier} = {i * multiplier}')

# 4. Написати Python-скрипт, який виводить на екран прямокутник із '*'.
# Висота і ширина прямокутника вводяться з клавіатури.
# Наприклад, нижче представлений прямокутник з висотою 4 та шириною 5

h, w = int(input('Enter height')),\
       int(input('Enter weight'))

if h < 3 or w < 3:
    print('WRONG: Height and width must be greater than 2')
else:
    i = 0
    while (i := i + 1) <= h:
        print(f'{" " * (w - 2):*^{w}}' if 1 < i < h else '*' * w)

# 5. Є список [0,5,2,4,7,1,3,19]. Написати Python-скрипт для підрахунку непарних цифр у ньому

num_list = [randint(1, 100) for _ in range(10)]
odd_num = '13579'

count = 0
text = ''.join(map(str, num_list))
for i in odd_num:
    count += text.count(i)
print(f'\nAmount of odd numbers = {count}\n')

# 6. Створіть список випадкових чисел (розміром 4 елементи). Створіть другий список
# у два рази більше першого, де перші 4 елементи повинні дорівнювати елементам
# першого списку, а решта елементів - подвоєним значенням початкових.

first_list = [randint(1, 100) for _ in range(4)]

res_list = first_list + [i * 2 for i in first_list]
print(f'Initial list = {first_list}\nResulted list = {res_list}\n')

# 7. Створіть список із 12 елементів. Кожен елемент цього списку є зарплатою робітника за місяць.
# Виведіть цей список на екран та обчисліть середньомісячну зарплату цього робітника.

payroll = [randint(10_000, 20_000) for _ in range(12)]

for k, i in enumerate(payroll):
    print(f'salary for the {k + 1} month = {i}')
print(f'Median salary per year = {sum(payroll) / len(payroll):.2f}\n')

# 8. Є матриця
# Напишіть Python-скрипт, який виведе цю матрицю на екран, обчислить та виведе суму елементів цієї матриці.

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

print(f'{"matrix":=^{LINE_WIDTH}}'.upper())
for i in matrix:
    print(f'{"   ".join(map(str, i)):^{LINE_WIDTH}}')
print(f'{"sum matrix = " + str(sum(sum(m) for m in matrix)):=^{LINE_WIDTH}}\n'.upper())

# 9. Написати код для дзеркального перевороту списку [7,2,9,4] -> [4,9,2,7].
# Список може бути довільною довжиною.

initial_list = [7, 2, 9, 4]

reversed_list = [i for i in reversed(initial_list)]
print(f'Initial list = {initial_list}\nReversed list = {reversed_list}\n')

# 10. За допомогою циклів вивести на екран усі прості числа від 1 до 100.

numb = input('Enter number for prime numbers')

print(f'{"prime numbers from 1 to " + numb:^{LINE_WIDTH}}'.upper())
for i in range(2, int(numb) + 1):
    print(not i % LINE_WIDTH and '\n' or '', end='')
    k = 1
    while (k := k + 1) < i:
        if not i % k:
            break
    else:
        print(i, end=', ')
print(f'\n{"end":^{LINE_WIDTH}}\n'.upper())

# better solution
# if i % 2 and i % 3 and i % 5 and i % 7 or i in (2, 3, 5, 7):

# 11. Виведіть на екран «пісочний годинник», максимальна ширина якого
# зчитується з клавіатури (число непарне). У прикладі ширина дорівнює 5.

num = int(input('Enter odd number for the clock'))

if num % 2:
    i = num
    while i > 1:
        print(f'{"*" * i:^{num}}')
        i -= 2
    while i <= num:
        print(f'{"*" * i:^{num}}')
        i += 2
else:
    print('WRONG: Given number is even')
