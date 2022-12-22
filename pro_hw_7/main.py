from modules import geometric_progression, number_generator, prime_numbers


if __name__ == '__main__':
    print(geometric_progression(3, 1000, 4))
    print(geometric_progression(3, 1000, 10))

    print(*range(-10, -5, 3))
    print(*number_generator(-10, -5, 3))

    print(*prime_numbers(100))

    third_degree_numbers_generator = map(lambda i: i ** 3, range(2, 25))
    print(*third_degree_numbers_generator)
