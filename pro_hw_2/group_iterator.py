class GroupIterator:
    def __init__(self, data_students):
        self.data_students = tuple(data_students)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data_students):
            self.index += 1
            return self.data_students[self.index - 1]
        raise StopIteration
