from datetime import datetime


# 1) Создайте дескриптор, который будет делать поля класса управляемые им доступными только для чтения.

# 2) Реализуйте функционал, который будет запрещать установку полей класса любыми значениями, кроме целых чисел.
# Т.е., если тому или иному полю попытаться присвоить, например, строку, то должно быть возбужденно исключение.

# 3) Реализуйте свойство класса, которое обладает следующим функционалом: при установке значения этого свойства в файл с
# заранее определенным названием должно сохранятся время (когда устанавливали значение свойства) и установленное значение.
class FixedHeightDescriptor:
    def __get__(self, obj, type=None):
        return obj._height


class ControlWidthDescriptor:
    NAME_FIELD = 'width'

    def __get__(self, obj, type=None):        return obj._width

    def __set__(self, obj, value):
        try:
            if not isinstance(value, int):
                raise TypeError(type(value), value)
            if value <= 0:
                raise ValueError(value)
            obj._width = value
        except (TypeError, ValueError) as ex:
            with open('exception.txt', 'a') as f:
                f.write(f'{datetime.now().strftime("%Y-%m-%d  %H:%M:%S")} '
                        f'Field: "{ControlWidthDescriptor.NAME_FIELD}". {type(ex).__name__}: {ex}\n')


class LoggerControlLengthDescriptor:
    NAME_FIELD = 'length'

    def __get__(self, obj, type=None):
        return obj._length

    def __set__(self, obj, value):
        try:
            if not isinstance(value, int):
                raise TypeError(type(value), value)
            if value <= 0:
                raise ValueError(value)
            obj._length = value
            with open('changing_class_fields.txt', 'a') as f:
                f.write(f'{datetime.now().strftime("%Y-%m-%d  %H:%M:%S")} '
                        f'Field: "{LoggerControlLengthDescriptor.NAME_FIELD}". Set the value: {obj._length}\n')
        except (TypeError, ValueError) as ex:
            with open('exception.txt', 'a') as f:
                f.write(f'{datetime.now().strftime("%Y-%m-%d  %H:%M:%S")} '
                        f'Field: "{LoggerControlLengthDescriptor.NAME_FIELD}". {type(ex).__name__}: {ex}\n')


class Box:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    length = LoggerControlLengthDescriptor()
    width = ControlWidthDescriptor()
    height = FixedHeightDescriptor()

    def __str__(self):
        return f'Box with parameters (L x W x H): {self._length} x {self._width} x {self._height}.'
