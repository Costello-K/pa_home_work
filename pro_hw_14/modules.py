import re


def search_regular_expressions_in_text(pattern, text):
    match = re.findall(pattern, text)
    if match:
        return tuple(match)
    raise ValueError(pattern)


def is_card_number_valid(card_number):
    if re.fullmatch(r'\d{4}([- ]?\d{4}){3}', card_number):
        return True
    raise ValueError(card_number)


def is_mail_valid(mail):
    if re.fullmatch(r'[\da-zA-Z](-?[_\da-zA-Z])*-?@([\da-zA-Z]+\.)*[a-z]{2,6}', mail):
        return True
    raise ValueError(mail)


def is_login_valid(login):
    if re.fullmatch(r'[\da-zA-Z]{2,10}', login):
        return True
    raise ValueError
