from math import sqrt


# 1. Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком».
# Примітка: щасливим квитком називається число, у якому, при парній кількості цифр,
# сума цифр його лівої половини дорівнює сумі цифр його правої половини.
# Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2.

num = input('Enter an even number')
if not len(num) % 2:
    ticket_len = int(len(num) / 2)
    happy_tic = sum(int(i) for i in num[:ticket_len]) == sum(int(i) for i in num[ticket_len:])
    print(f'This number is{happy_tic and " " or " un"}lucky')
else:
    print(f'Given number is not even')

# 2. З клавіатури вводиться число (шестизначне). Перевірити, чи воно є паліндромом.
# Примітка: Паліндром називається число, слово або текст, які однаково читаються зліва направо і справа наліво.
# Наприклад, це числа 143341, 5555, 7117 і т.д.

numb = input('Enter number')
print(f'Entered number is{numb == numb[::-1] and " " or " not "}palindrome')

# 3. Дано коло з центром на початку координат та радіусом 4. Користувач вводить з клавіатури
# координати точки x та y. Написати програму, яка визначить, лежить ця точка всередині кола чи ні.

R = 4

x, y = float(input('Enter coordinate x')),\
       float(input('Enter coordinate y'))

dist = sqrt(x ** 2 + y ** 2)
print(f'The point with the given coordinate is located {dist <= R and "inside" or "outside"} the circle')
