from modules import search_regular_expressions_in_text, is_card_number_valid, is_mail_valid, is_login_valid


if __name__ == '__main__':
    try:
        print(search_regular_expressions_in_text(r'Rb+r', 'RRbbbrr'))
        print(search_regular_expressions_in_text(r'Rb+r', 'RRbrrRbbbr'))
        print(search_regular_expressions_in_text(r'Rb+r', 'RRrrrRbbbrRRbbbrrRbbbrRbbbrRbbbr'))
        print(search_regular_expressions_in_text(r'Rb+r', 'Rrr'))
    except Exception as ex:
        print(f'Regular Expressions "{ex}" in the text not found')

    print('*' * 50)

    try:
        print(is_card_number_valid('1111 9999 9999 9999'))
        print(is_card_number_valid('0000223499999999'))
        print(is_card_number_valid('8999-9999-6785-9998'))
        print(is_card_number_valid('yf8999-9999-6785-9998'))
    except Exception as ex:
        print(f'"{ex}" is not a credit card number')

    print('*' * 50)

    try:
        print(is_mail_valid('fdghfg5@gmail.com'))
        print(is_mail_valid('f-d___g-h-fg5-@gmail.com'))
        print(is_mail_valid('f-d___g-h-fg5-@i.gmail.com'))
        print(is_mail_valid('f-d___g-h-fg5-@com'))
        print(is_mail_valid('f-d___g-h-fg5-@gmail.com'))
        print(is_mail_valid('fdghfg5--@gmail.com'))
    except Exception as ex:
        print(f'This mail is invalid: "{ex}"')

    print('*' * 50)

    try:
        print(is_login_valid('567yyyy'))
        print(is_login_valid('-jghfhf7'))
        print(is_login_valid('45dfghfghtyu76'))
    except:
        print(f'This login is invalid')
