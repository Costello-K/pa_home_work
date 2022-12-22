import abc


# 1) Создайте ABC класс с абстрактным методом проверки целого числа на простоту. Т.е., если параметром этого метода
# является целое число и оно простое, то метод должен вернуть True, а в противном случае False.

# 2) Создайте класс его наследующий.

# 3) Создайте класс, который не наследует пользовательский ABC класс, но обладает нужным методом.
# Зарегистрируйте его в качестве виртуального подкласса.

# 4) Проверьте работоспособность проекта.
class AbstractClass(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def is_prime_numbers(number):
        ...


class InheritanceAbstractClass(AbstractClass):

    @staticmethod
    def is_prime_numbers(number):
        if not isinstance(number, int):
            raise TypeError
        return True if number % 2 and number % 3 and number % 5 and number % 7 or number in (2, 3, 5, 7) else False


class NotInheritingAbstractClass:

    @staticmethod
    def is_prime_numbers(number):
        if not isinstance(number, int):
            raise TypeError
        return True if number % 2 and number % 3 and number % 5 and number % 7 or number in (2, 3, 5, 7) else False
