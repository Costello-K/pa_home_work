from random import randint
from string import ascii_lowercase
from modules import *
from human import Human


if __name__ == '__main__':
    print(get_text_1('text1'))
    print(get_text_1('text1'))
    print(get_text_1('text1'))

    print(get_text_2('text2'))
    print(get_text_2('text2'))

    print(get_text_1.count)
    print(get_text_2.count)

    print('*' * 100)

    func_1([i for i in range(100)])
    func_1([i for i in range(200)])
    func_2([i for i in range(200)])
    func_3(dict(zip(ascii_lowercase, range(1, 27))))

    print(list_function_for_list, list_function_for_tuple, list_function_for_set, list_function_for_dict, sep='\n')

    print('*' * 100)

    human_1 = Human('Petro', 'Petrov')
    human_2 = Human('Ivan', 'Ivanov')
    human_3 = Human('Alex', 'Toh')

    print(human_1, human_2, human_3, sep='\n')

    print(func_4())
