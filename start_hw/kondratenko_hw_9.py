import string
from random import *


# 1. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери,
# які є одночасно і в першому, і в другому рядку. Наприклад,
# для рядків «Hello» та «World» на екрані мають бути літери «l» та «o».

first_list, second_list = input('Enter text'), input('Enter text')


def general_symbols(text_a, text_b):
    if isinstance(text_a, str) and isinstance(text_b, str):
        return ''.join(set(text_a) & set(text_b))
    raise TypeError('WRONG Type')


print(general_symbols(first_list, second_list))

# 2. Напишіть програму, яка згенерує два списки.
# Один із числами кратними 3, інший із числами кратними 5.


def generation_set(multiple):
    if isinstance(multiple, int):
        return {randint(1, 50) * multiple for _ in range(100)}
    raise TypeError('WRONG Type')


first_list, second_list = generation_set(3), generation_set(5)

# 3. Створіть список із числами, які є в обох списках.
# Напишіть функцію, яка поверне максимальне число зі списку чисел.

all_list = tuple(first_list & second_list)

# without using the function max()


def max_number(data):
    if not isinstance(data, tuple | list):
        raise TypeError('WRONG Type')

    max_num = data[0] or None
    for i in data:
        if i > max_num:
            max_num = i
    return max_num


print(max_number(all_list))

# 4. Реалізуйте функцію, параметрами якої є два числа та рядок.
# Повертає вона конкатенацію рядка із сумою чисел.


def data_to_string(text, *args):
    sum_numb = sum(args)
    if isinstance(sum_numb, int | float) and isinstance(text, str):
        return f'{sum_numb:.2f}{text}'
    raise TypeError('WRONG Type')


print(data_to_string('text', 3.562, 6))

# 5. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
# Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.


def print_string(w, space=' '):
    if isinstance(w, int):
        return f'*{space * (w - 2)}*'
    raise TypeError('WRONG Type')


def figure(h, w):
    if h < 3 or w < 3:
        raise ValueError('WRONG: Height and width must be greater than 2')
    if not isinstance(h, int) and not isinstance(w, int):
        raise TypeError('WRONG Type')

    res = []
    while len(res) < h:
        res.append(print_string(w, '*') if not res or len(res) == h - 1 else print_string(w))
    return '\n'.join(res)


print(figure(4, 4))

# 6. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».


def find_index(seq, element):
    if not isinstance(sum(seq), int) and not isinstance(element, int):
        raise TypeError('WRONG Type')

    for index, item in enumerate(seq):
        if item == element:
            return index

    return -1


arr = [0, 4, 11]

print(find_index(arr, 12))

# 7. Напишіть функцію, яка поверне кількість слів у текстовому рядку.


def del_symbol_punctuation(text, punctuation):
    if not isinstance(text, str) and not isinstance(punctuation, str):
        raise TypeError('WRONG Type')

    punctuation = set(text) & set(punctuation)
    for i in punctuation:
        while i in text:
            text = text.replace(i, '')
    return text


def count_words(text):
    if not isinstance(text, str):
        raise TypeError('WRONG Type')

    return len(del_symbol_punctuation(text, string.punctuation).split())


print(count_words('   My   ag;e - 55 '))
