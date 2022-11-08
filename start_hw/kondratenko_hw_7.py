from math import pi


# 1. Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту.

print(f'String contains {input("Enter text").count("b")} symbols "b"')

# 2. Користувач вводить з клавіатури ім'я людини. Написати програму для перевірки
# введеного ім'я на валідність (мається на увазі, що, наприклад, в імені людини не
# може бути цифр, воно повинно починатися з великої літери, за якою повинні йти маленькі).

name = input('Enter name').strip()

print(f'{"Correct" if len(name) > 2 and name.istitle() else "Incorrect"} name')

# 3. Напишіть програму, яка обчислить суму всіх кодів символів рядка.

print(f'The sum of the codes of all symbols: {sum(map(ord, input("Enter text")))}')

# 4. Виведіть на екран 10 рядків із значенням числа Pi. У першому рядку має бути
# 2 знаки після коми, у другому 3 і так далі.

for i in range(2, 12):
    print(f'Pi = {pi:.{i}f}')

# 5. Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та
# вивести його на екран.

text = input('Enter text').split()

print(f'Most largest word in string: {max(text, key=len)}')

# 6. Вовочка, сидячи на уроці, писав поспіль однакові слова (слово може складатися
# з однієї літери). Коли Марія Іванівна забрала у нього зошит, там був один рядок тексту.
# Напишіть програму, яка визначить найкоротше слово з написаних Вовочкою. Наприклад:
# aaaaaaa - Вовочка писав слово - "a"
# catcatcatcat - Вовочка писав слово - "cat"

text = 'hghgffhghgff'

word = ''
for i in range(1, len(text) // 2):
    if text.count(text[0:i]) == len(text) / i:
        word = text[:i]
        break
else:
    word = text

print(f'Word: {word}')

# 7. Напишіть програму для очищення тексту від HTML-тегів. Більше про
# html-теги https://html5book.ru/html-tags/
# Також необхідно врахувати кілька особливостей:
# - крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває,
# а другий закриває.
# - тег у собі може містити купу додаткової інформації.
# Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">

text = ' <div id="rcnt" style="clear:both;position:relative;zoom:1"> 1<11>1 </div>' \
       '<div id="rcnt" style="clear:both;position:relative;zoom:1"></div>' \
       '2222222<div id="rcnt" style="clear:both;position:relative;zoom:1"> 333333 </div>'

tag_list = ['a', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'img', 'b', 'body',
            'em', 'form', 'head', 'i', 'li', 'link', 'ol', 'p', 'span', 'td',
            'th', 'title', 'u', 'ul', 'var']

for tag in tag_list:
    text = text.replace(f'</{tag}>', '')

    while f'<{tag}' in text:
        ind_start = text.find(f'<{tag}')
        ind_end = text.find('>', ind_start)
        text = text.replace(text[ind_start:ind_end + 1], '')

print(f'New string: "{text}"')

