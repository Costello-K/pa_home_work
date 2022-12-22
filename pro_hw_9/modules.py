from datetime import datetime
from logger import logger


list_function_for_list = {}
list_function_for_tuple = {}
list_function_for_set = {}
list_function_for_dict = {}


# 1. Создайте декоратор, который будет подсчитывать, сколько раз была вызвана декорируемая функция.
def decorator(func):
    def inner(*args, **kwargs):
        inner.count += 1
        return f'<decorator {inner.count}>___{func(*args, **kwargs)}___</decorator {inner.count}>'
    inner.count = 0
    return inner


@decorator
def get_text_1(text):
    return f'{text}'


@decorator
def get_text_2(text):
    return f'{text}'


# 2. Создайте декоратор, который зарегистрирует декорируемую функцию в списке функций, для обработки последовательности.
def function_registration(func):
    def inner(*args, **kwargs):
        try:
            if isinstance(*args, list) and func.__name__ not in list_function_for_list:
                list_function_for_list[func.__name__] = func
            elif isinstance(*args, tuple) and func.__name__ not in list_function_for_tuple:
                list_function_for_tuple[func.__name__] = func
            elif isinstance(*args, set) and func.__name__ not in list_function_for_set:
                list_function_for_set[func.__name__] = func
            elif isinstance(*args, dict) and func.__name__ not in list_function_for_dict:
                list_function_for_dict[func.__name__] = func
            else:
                raise ValueError
        except:
            # logging to file
            ...
        finally:
            return func(*args, **kwargs)

    return inner


@function_registration
def func_1(seq: list) -> tuple:
    return tuple(map(lambda i: i ** 5 + 100, seq))


@function_registration
def func_2(seq: list) -> tuple:
    return tuple(map(lambda i: i ** 2 + 100, seq))


@function_registration
def func_3(seq: dict) -> tuple:
    return tuple(map(lambda i: f'{i}_{seq[i]}', seq))


@function_registration
def func_3(seq: dict) -> tuple:
    return tuple(map(lambda i: f'{i}_{seq[i]}', seq))


# 3 - used in 'human.py' file
# Предположим, в классе определен метод __str__, который возвращает строку на основании класса.
# Создайте такой декоратор для этого метода, чтобы полученная строка сохранялась в текстовый файл, имя которого
# совпадает с именем класса, метод которого вы декорировали.
def save_result_to_file(func):
    def inner(*args, **kwargs):
        # str(func).split()[1].split(".")[0]
        with open(f'{args[0].__class__.__name__}.txt', 'a') as f:
            f.write(f'{func(*args, **kwargs)}\n')
        return func(*args, **kwargs)
    return inner


# 4. Создайте декоратор с параметрами для проведения хронометража работы той или иной функции.
# Параметрами должны выступать то, сколько раз нужно запустить декорируемую функцию и в какой файл сохранить
# результаты хронометража. Цель - провести хронометраж декорируемой функции.
def logger_decorator(quantity_iterations):
    def outer(func):
        def inner(*args, **kwargs):
            start = datetime.now()
            for _ in range(quantity_iterations):
                func(*args, **kwargs)
            finish = datetime.now()
            logger.info(f'Function start at {start}, finish at {finish}, {quantity_iterations} iterations. '
                        f'Total time: {finish - start}')
            return func(*args, **kwargs)
        return inner
    return outer


@logger_decorator(10)
def func_4(n=10000000):
    while n := n - 1:
        ...
    return n
