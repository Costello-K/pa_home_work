from modules import Box


if __name__ == '__main__':
    box_1 = Box(1, 2, 3)
    box_2 = Box(1, 2, 3)

    # trying to change height
    box_1.height = 100

    print('box_1', box_1)
    print('box_2', box_2)
    print(box_1.length, box_1.width, box_1.height)
    print(box_2.length, box_2.width, box_2.height)

    box_3 = Box(1, 2, 3)

    box_1.width = 200
    box_1.width = -200
    box_1.length = 300

    print('box_1', box_1)
    print('box_2', box_2)
    print('box_3', box_3)
    print(box_1.length, box_1.width, box_1.height)
    print(box_2.length, box_2.width, box_2.height)
    print(box_3.length, box_3.width, box_3.height)

    box_1.length = 200
    box_1.length = 50
    box_1.length = '50'
    box_1.length = 10

    # trying to change height
    box_1.height = 100
    box_2.height = 100

    box_1.length = 15
    box_1.length = 20
    box_2.length = 1000

    print('box_1', box_1)
    print('box_2', box_2)
    print('box_3', box_3)
    print(box_1.length, box_1.width, box_1.height)
    print(box_2.length, box_2.width, box_2.height)
    print(box_3.length, box_3.width, box_3.height)
