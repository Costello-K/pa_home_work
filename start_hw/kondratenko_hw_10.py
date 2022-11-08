import operator

operation = {
    '+': operator.add,
    '*': operator.mul,
    '**': operator.pow
}


# 1. Існують такі послідовності чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. Наприклад, користувач вводить рядок
# 0,5,10,15,20,25 та відповіддю програми має бути число 30.

# def hhh()
#
# def next_number(actions, *args):
#     li = args
#
#     for i in actions:
#         action = actions[i]
#         k, n = 0, 0
#         while k < len(li):
#             while n <= li[1] - li[0]:
#                 if li[k+1] and action(li[k], n) == li[k+1]:
#                     return action(li[-1], n)
#                 n += 1
#             k += 1
#             n = 0
#         else:
#             return action(li[-1], n)


# print(next_number(operation, 0, 2, 4, 6, 8, 10, 12))# 14
# print(next_number(operation, 1, 4, 7, 10, 13))# 16
# print(next_number(operation, 1, 2, 4, 8, 16, 32))# 64
# print(next_number(operation, 1, 3, 9, 27))# 81
# print(next_number(operation, 1, 4, 9, 16, 25))# 36
# print(next_number(operation, 1, 8, 27, 64, 125))#216

# 2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, vyj;tyyzv яких чисел він є.


def palindrome(number):
    numb_one = numb_two = number
    numb_one =
    while numb_one and numb_two:
        product = numb_one * numb_two
        text = str(product)
        half_len = len(text) // 2
        if text[:half_len] != text[:-half_len-1:-1]:
            if (numb_one - 1) * numb_two >= (numb_two - 1) * numb_one:
                numb_one -= 1
            else:
                numb_two -= 1
        else:
            return f'{numb_one} x {numb_two} = {product}'
    raise ValueError('WRONG: Not have palindrome')


print(palindrome(99))
