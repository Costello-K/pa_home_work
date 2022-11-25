from dict import days_week, dict_cats, dict_numbers, roman_numerals

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


def degree(stack_number, dictionary, digit_position=None):
    number, tens, num_degree = dictionary.keys()
    res = []
    if stack_number // 100:
        res.append(f'{dictionary[number][stack_number // 100]} hundred')
    if stack_number % 100 < 20:
        res.append(f'{dictionary[number][stack_number % 100]}')
    else:
        res.append(f'{dictionary[tens][stack_number % 100 // 10]}')
        if dictionary[number][stack_number % 10]:
            res.append(f'{dictionary[number][stack_number % 10]}')
    if digit_position:
        res.append(f'{dict_numbers[num_degree][digit_position]}')
    return res


def get_words_from_num(number: str | int | float):
    if not isinstance(number, str | int | float):
        raise TypeError('WRONG Type')
    if int(number) < 0:
        raise ValueError('WRONG Value')

    num_to_tuple = tuple(map(int, str(f'{number: .2f}').replace('.', ',').split(',')))
    dollar = []

    dollar_to_list = '{0:,}'.format(num_to_tuple[0]).replace(',', ' ').split()
    for k, v in enumerate(dollar_to_list):
        if int(v):
            dollar += degree(int(v), dict_numbers, len(dollar_to_list) - k)

    return f'{" ".join(dollar) or "zero"} dollars {" ".join(degree(num_to_tuple[1], dict_numbers)) or "zero"} cents'


print(get_words_from_num(1_999_995_640.50))

# 5. Напишіть програму, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22


def get_decimal_from_roman(roman_number: str, date_numerals: dict):
    if not isinstance(roman_number, str):
        raise TypeError('WRONG Type')

    if set(roman_number) - set(date_numerals) or not roman_number:
        raise ValueError('WRONG Value')

    decimal_number = date_numerals[roman_number[-1]]
    for i, k in zip(roman_number, roman_number[1:]):
        decimal_number += -date_numerals[i] if date_numerals[i] < date_numerals[k] else date_numerals[i]

    return decimal_number


print(get_decimal_from_roman('DCCLXXXIX', roman_numerals))
