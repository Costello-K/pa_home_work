import timeit
from modules import geometric_progression, fourth_degree, sum_numbers, s_1, s_2


if __name__ == '__main__':
    print(*geometric_progression(lambda i: i + 10, 3, 100, 4))
    # print(*geometric_progression(lambda i: i * 22, 3, 100_000, 5))

    print(timeit.timeit(s_1, number=5))
    print(timeit.timeit(s_2, number=5))

    print(sum_numbers(fourth_degree, (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
