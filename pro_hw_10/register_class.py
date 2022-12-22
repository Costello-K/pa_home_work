classlist = {}


# 1) Создайте декоратор, который зарегистрирует декорируемый класс в списке  классов.
def register_class(store):
    def outer(cls):
        try:
            if cls.__name__ in store:
                raise ValueError(f'Class "{cls.__name__}" is already registered. '
                                 f'Rename your class or specify a different dictionary to register the class')

            store[cls.__name__] = cls

            def inner(*args, **kwargs):
                return cls(*args, **kwargs)
            return inner
        except ValueError:
            # logging to file
            ...
    return outer


@register_class(classlist)
class Empty:
    @staticmethod
    def empty():
        return 'empty_1'


@register_class(classlist)
class Nothing:
    @staticmethod
    def nothing():
        return 'nothing'


@register_class(classlist)
class Empty:
    @staticmethod
    def empty():
        return 'empty_2'
