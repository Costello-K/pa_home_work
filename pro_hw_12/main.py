from modules import Box, Point

if __name__ == '__main__':
    print(Box, Box.__class__)  # <class '__main__.Box'> <class '__main__.MetaClass'>

    box_1 = Box(3)
    print(box_1)

    box_2 = Box(6)
    print(box_2)

    point_1 = Point(1)
    print(point_1)

    point_2 = Point(2)
    print(point_2)
