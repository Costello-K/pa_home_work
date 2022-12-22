# 2) Создайте декоратор класса с параметром. Параметром должна быть строка, которая должна  дописываться (слева)
# к результату работы  метода __str__.
def add_str_left_class(text):
    def outer(cls):
        origin_str_of_class = cls.__str__

        def inner(*args, **kwargs):
            return f'{text} {origin_str_of_class(*args, **kwargs)}'

        cls.__str__ = inner
        return cls
    return outer


# Ivan's variant. START
def new_method_str(origi_method_str, text):
    def inner(*args, **kwargs):
        return f'{text} {origi_method_str(*args, **kwargs)}'
    return inner


def add_str_left_class_2(text):
    def outer(cls):
        cls.__str__ = new_method_str(cls.__str__, text)

        def inner(*args, **kwargs):
            return cls(*args, **kwargs)
        return inner
    return outer
# END


@add_str_left_class('Apply decorator')
class Text:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


@add_str_left_class_2('Apply decorator 2')
class TextIvan:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text
