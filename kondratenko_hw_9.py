import string
from random import *


# 1. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери,
# які є одночасно і в першому, і в другому рядку. Наприклад,
# для рядків «Hello» та «World» на екрані мають бути літери «l» та «o».

first_list, second_list = input('Enter text'), input('Enter text')


def general_symbols(text_a: str, text_b: str):
    if isinstance(text_a, str) and isinstance(text_b, str):
        return ''.join(set(text_a) & set(text_b))
    raise TypeError('WRONG Type')


print(general_symbols(first_list, second_list))

# 2. Напишіть програму, яка згенерує два списки.
# Один із числами кратними 3, інший із числами кратними 5.


def generation_set(multiple: int):
    if isinstance(multiple, int):
        return {randint(1, 50) * multiple for _ in range(100)}
    raise TypeError('WRONG Type')


first_list, second_list = generation_set(3), generation_set(5)

# 3. Створіть список із числами, які є в обох списках.
# Напишіть функцію, яка поверне максимальне число зі списку чисел.

all_list = tuple(first_list & second_list)

# without using the function max()


def max_number(data: tuple | list):
    if isinstance(data, tuple | list):
        max_num = data[0]
        for i in data:
            if i > max_num:
                max_num = i
        return max_num
    raise TypeError('WRONG Type')


print(max_number(all_list))

# 4. Реалізуйте функцію, параметрами якої є два числа та рядок.
# Повертає вона конкатенацію рядка із сумою чисел.


def data_to_string(text: str, *kwargs: int | float):
    sum_numb = sum([*kwargs])
    if isinstance(sum_numb, int | float) and isinstance(text, str):
        return f'{sum_numb:.2f}{text}'
    raise TypeError('WRONG Type')


print(data_to_string('text', 3.562, 6))

# 5. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
# Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.


def print_string(w: int, space=' '):
    if isinstance(w, int):
        print(f'*{space * (w - 2)}*')
        return None
    raise TypeError('WRONG Type')


def figura(h: int, w: int):
    if h < 3 or w < 3:
        raise ValueError('WRONG: Height and width must be greater than 2')
    if isinstance(h, int) and isinstance(w, int):
        i = 0
        while (i := i + 1) <= h:
            print_string(w) if 1 < i < h else print_string(w, '*')
        return None
    raise TypeError('WRONG Type')


figura(4, 4)

# 6. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».


def find_r(data: list, element):
    if isinstance(sum(data), int) and isinstance(element, int):
        index = 0
        for i in data:
            if i == element:
                return index
            index += 1
        return -1
    raise TypeError('WRONG Type')


arr = [0, 4, 11]

print(find_r(arr, 12))

# 7. Напишіть функцію, яка поверне кількість слів у текстовому рядку.


def del_symbol_punctuation(text: str, punctuation: str):
    if isinstance(text, str) and isinstance(punctuation, str):
        punctuation = set(text) & set(punctuation)
        for i in punctuation:
            while i in text:
                text = text.replace(i, '')
        return text
    raise TypeError('WRONG Type')


def count_words(text: str):
    if isinstance(text, str):
        return len(del_symbol_punctuation(text, string.punctuation).split())
    raise TypeError('WRONG Type')


print(count_words(' My ag;e - 55 '))
