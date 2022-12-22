import os


# 1) Реализуйте метакласс, который обладает следующим функционалом: при его использовании в файл
# с заранее определенным названием нужно сохранить имя класса и список его полей.
class CustomMetaClass(type):
    def __new__(mcs, class_name, supers_tuple, attribute_class_dict):
        data = []
        is_replace = False

        if os.path.isfile('class_list.txt'):
            with open('class_list.txt', 'r') as f:
                data = [line.strip() for line in f]

        with open('class_list.txt', 'a') as f:
            new_class_name = f'ClassName: "{class_name}"'
            new_list_fields = f'Fields of class "{class_name}": {tuple([*attribute_class_dict.keys()])}'
            if not data or new_class_name not in data:
                f.writelines(f'{new_class_name}\n')
                f.writelines(f'{new_list_fields}\n')
            elif new_list_fields not in data:
                data[data.index(new_class_name) + 1] = new_list_fields
                is_replace = True

        if is_replace:
            with open('class_list.txt', 'w') as f:
                f.write('\n'.join(data))
                f.write('\n')

        return type.__new__(mcs, class_name, supers_tuple, attribute_class_dict)


class Box(metaclass=CustomMetaClass):
    field_1 = 100
    field_2 = 200
    field_3 = 200

    def __init__(self, x):
        self.x = x
        self.y = Box.field_1
        self.z = Box.field_2

    def __str__(self):
        return f'Box: {self.x} x {self.y} x {self.z}'


class Point(metaclass=CustomMetaClass):
    field_1 = 100

    def __init__(self, x):
        self.x = x
        self.y = Point.field_1

    def __str__(self):
        return f'Point: ({self.x}, {self.y})'
