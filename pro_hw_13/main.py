from modules import AbstractClass, NotInheritingAbstractClass


if __name__ == '__main__':
    exemplar = NotInheritingAbstractClass()
    print(isinstance(exemplar, AbstractClass))

    AbstractClass.register(NotInheritingAbstractClass)
    print(isinstance(exemplar, AbstractClass))
