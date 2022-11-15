from logger import logger
from exceptions import InvalidArgument, ExceedingTheLimit
from student import Student
from group_iterator import GroupIterator


class Group:
    """
    Group of students
    Supports methods for adding, deleting, searching students by surname
    """

    def __init__(self, title: str, max_students=10):
        """
        :param title: group name
        :param max_students: maximum number of students in group
        """
        self.title = title
        self.__students = []
        self.__max_students = max_students

    def __str__(self):
        if self.__students:
            return f'Group: {self.title}\n\t' + '\n\t'.join(map(str, self.__students))
        return 'There are no students in the group'

    def __iter__(self):
        return GroupIterator(self.__students)

    def __len__(self):
        return self.__students.__len__()

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < self.__students.__len__():
                return self.__students[index]
            raise IndexError
        if isinstance(index, slice):
            start = index.start or 0
            stop = index.stop or self.__students.__len__()
            step = index.step or 1
            res = []
            for i in range(start, stop, step):
                res.append(self.__students[i])
            return res
        raise TypeError

    def add_student(self, student: Student):
        if not isinstance(student, Student):
            logger.warning(f'{student}: Wrong datatype with student')
            raise InvalidArgument(f'"{student}" is not an instance of class Student')
        if len(self.__students) == self.__max_students:
            logger.warning(f'{student}: Limit')
            raise ExceedingTheLimit(f'Maximum number of students in group = {self.__max_students}')
        if student not in self.__students:
            logger.info(f'{student}: add to group {self.title}')
            self.__students.append(student)

    def del_student(self, student: Student):
        if not isinstance(student, Student):
            raise InvalidArgument(f'"{student}" is not an instance of class Student')
        if student in self.__students:
            self.__students.remove(student)

    def search_surname(self, surname: str):
        return [i for i in self.__students if i.surname == surname] or None

