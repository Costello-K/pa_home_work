from register_class import classlist
from box import Box
from decorator_change_str_class import Text, TextIvan


if __name__ == '__main__':
    print(classlist)

    print(Text('Test'))
    print(Text('New text'))

    print(TextIvan('Test'))
    print(TextIvan('New text'))

    box_1 = Box(4, 5, 5)
    box_2 = Box(5, 6, 6)
    box_3 = Box(10, 10, 6)

    print(Box.sum_volume(box_1, box_2, box_3))
