from dict import *

# 1. Використовуючи словник, напишіть програму, яка виведе на екран назву дня тижня за номером.
# Наприклад, 1 - "Monday".


def get_day_week(day_number, dictionary):
    res = dictionary.get(int(day_number))
    if res:
        return res
    raise ValueError('WRONG Value')


print(get_day_week(input('Enter the number of the day of the week from 1 to 7'), days_week))

# 2. Опишіть кота (домашня тварина) на основі словника.


def add_cat(dictionary):
    name, age, seria, number = input('Name - '),\
                               input('Age - '),\
                               input('Passport seria - '),\
                               input('Passport number - ')
    cat = {'name': name, 'age': age, "passport": {'seria': seria, 'number': number}}
    dictionary.append(cat)
    return None


add_cat(dict_cats)

for item in dict_cats:
    print(f'Name: {item["name"]}, '
          f'age: {item["age"]}, '
          f'passport: {item["passport"]["seria"]+str(item["passport"]["number"])}')

# 3. Напишіть програму, яка читає рядок тексту з клавіатури і виводить на екран статистику,
# скільки разів яка літера зустрічається в цьому рядку.
# Наприклад, для рядка «Hello world» ця статистика виглядає так: «H» - 1, «e» - 1, «l» - 3 і т.д.


def get_count_literals(text):
    if isinstance(text, str):
        count_literals = {}
        for i in text:
            if not count_literals.get(i):
                count_literals[i] = text.count(i)
        if ' ' in count_literals:
            del count_literals[' ']
        return count_literals
    raise TypeError('WRONG Type')


print(get_count_literals(input('Enter text')))

# 4. Ввести з клавіатури число, що означає кількість доларів і центів. Вивести цю кількість прописом.
# Наприклад:
# How much money do you have?
# 123,34
# You have: one hundred twenty three dollars thirty four cents


def degree(numb, dictionary, var):
    if numb // 100:
        var.append(f'{dictionary["number"][numb // 100]} hundred')
    if numb % 100 < 20:
        var.append(f'{dictionary["number"][numb % 100]}')
    else:
        var.append(f'{dictionary["tens"][numb % 100 // 10]}')
        var.append(f'{dictionary["number"][numb % 10]}')
    return None


def get_words_from_num(number: str | int | float):
    if not isinstance(number, str | int | float):
        raise TypeError('WRONG Type')
    if int(number) < 0:
        raise ValueError('WRONG Value')
    num_to_list = list(map(int, str(f'{number: .2f}').replace('.', ',').split(',')))
    dollar, cent = [], []
    i = len(str(num_to_list[0])) // 3
    while i > -1:
        if not num_to_list[0]:
            dollar.append('zero')
            break
        num = int(str(num_to_list[0] // 10 ** (3 * i))[-3:])
        if num:
            degree(num, dict_numbers, dollar)
            dollar.append(f'{dict_numbers["degree"][i]}')
        i -= 1
    cent.append('zero') if not num_to_list[1] else degree(num_to_list[1], dict_numbers, cent)
    res = f'You have: {" ".join(dollar)} dollars {" ".join(cent)} cents'
    while '  ' in res:
        res = res.replace('  ', ' ')
    return res


print(get_words_from_num(99995640.50))

# 5. Напишіть програму, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22


def get_decimal_from_roman(roman_number: str):
    if not isinstance(roman_number, str):
        raise TypeError('WRONG Type')
    dict_keys = roman_numerals.keys()
    for i in roman_number:
        if i not in dict_keys or not i.isupper():
            raise ValueError('WRONG Value')
    decimal_number = roman_numerals[roman_number[-1]]
    for i, k in zip(roman_number, roman_number[1:]):
        if roman_numerals[i] >= roman_numerals[k]:
            decimal_number += roman_numerals[i]
        else:
            decimal_number -= roman_numerals[i]
    return decimal_number


print(get_decimal_from_roman('DCCLXXXIX'))
