from exceptions import *


class Human:
    """

    """

    def __init__(self, name: str, surname: str, date_birth: str):
        """
        :param name: student's name
        :param surname: student's surname
        :param date_birth: date of birth
        """
        self.name = name
        self.surname = surname
        self.date_birth = date_birth

    def __str__(self):
        return f'{self.name} {self.surname}, date of birth: {self.name}'


class Student(Human):
    """

    """

    def __init__(self, name: str, surname: str, date_birth: str, passport: str):
        """
        :param name: student's name
        :param surname: student's surname
        :param date_birth: date of birth
        :param passport: student passport number
        """
        super().__init__(name, surname, date_birth)
        self.passport = passport

    def __str__(self):
        return f'{self.name} {self.surname}. Passport: {self.passport}'


class Group:
    """

    """

    def __init__(self, title: str, max_students=10):
        """
        :param title: group name
        :param max_students: maximum number of students in a group
        """
        self.title = title
        self.__students = []
        self.__max_students = max_students

    def __str__(self):
        if self.__students:
            return f'Group: {self.title}\n\t' + '\n\t'.join(map(str, self.__students))
        return 'There are no students in the group'

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            raise InvalidArgument(f'"{student}" is not an instance of a class Student')
        if len(self.__students) == self.__max_students:
            raise ExceedingTheLimit(f'Maximum number of students in a group = {self.__max_students}')
        if student not in self.__students:
            self.__students.append(student)

    def del_student(self, student: Student):
        if not isinstance(student, Student):
            raise InvalidArgument(f'"{student}" is not an instance of a class Student')
        if student in self.__students:
            self.__students.remove(student)

    def search_surname(self, surname: str):
        return [i for i in self.__students if i.surname == surname] or None


s_1 = Student('Ли', 'Чу', '1999.01.07', 'КВ208347')
s_2 = Student('Ли2', 'Чун', '1999.02.21', 'КВ907341')
s_3 = Student('Ли3', 'Чао', '1999.03.16', 'КВ218542')
s_4 = Student('Ли4', 'Гао', '1999.04.06', 'КВ958349')
s_5 = Student('Ли5', 'Чад', '1999.05.25', 'КВ908346')
s_6 = Student('Ли6', 'Чан', '1999.06.30', 'КВ108342')
s_7 = Student('Ли7', 'Чад', '1999.07.12', 'КВ708746')
s_8 = Student('Ли8', 'Хун', '1999.08.03', 'КВ508346')
s_9 = Student('Ли9', 'Хо', '1999.09.30', 'КВ108346')
s_10 = Student('Ли10', 'Чук', '1999.10.08', 'КВ958379')
s_11 = Student('Ли11', 'Ч', '1999.10.08', 'КВ96789')

group_1 = Group('ПЦБ1')

try:
    group_1.add_student(s_1)
    group_1.add_student(s_2)
    group_1.del_student(s_2)
    group_1.add_student(s_2)
    group_1.add_student(s_5)
    group_1.add_student(s_6)
    group_1.add_student(s_7)
    group_1.add_student(s_8)
    group_1.add_student(s_9)
    group_1.add_student(s_10)
    group_1.add_student(s_4)
    group_1.add_student(s_3)
    group_1.add_student(s_11)
except:
    pass

print(group_1)
