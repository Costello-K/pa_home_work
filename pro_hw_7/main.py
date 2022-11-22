from moduls import geometric_progression, number_generator, prime_numbers


if __name__ == '__main__':
    seq_1 = geometric_progression(3, 1000, 4)
    seq_2 = geometric_progression(3, 1000, 10)
    print(*seq_2)

    print(*range(-10, -5, 3))
    print(*number_generator(-10, -5, 3))

    print(*prime_numbers(100))

    third_degree_numbers_generator = (i ** 3 for i in range(2, 25))
    print(*third_degree_numbers_generator)

