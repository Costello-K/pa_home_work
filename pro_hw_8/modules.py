def geometric_progression_generator(func, start, quantity_members):
    while quantity_members:
        res = yield start
        if res:
            return
        start = func(start)
        quantity_members -= 1


def geometric_progression(func, start: int, limit: int, quantity_members: int):
    if not all(map(lambda p: isinstance(p, int), (start, limit, quantity_members))):
        raise TypeError

    iteration, value = 0, 0
    try:
        seq = geometric_progression_generator(func, start, quantity_members)
        for k, v in enumerate(seq):
            if v >= limit:
                iteration, value = k, v
                seq.send('stop')
        return geometric_progression_generator(func, start, quantity_members)
    except StopIteration:
        print(f'Error. Sequence has reached iteration {iteration} with value: {value}')


s_1 = '''
def fibonacci_closure(number_members):
    a, b, n = 0, 1, number_members

    def next_member():
        nonlocal a, b, n
        n -= 1
        a, b = b, a + b
        while n:
            next_member()
        return a
    return next_member()


print(fibonacci_closure(10))
'''

s_2 = '''
def fibonacci_recursion(number_members):
    if number_members in (1, 2):
        return 1
    return fibonacci_recursion(number_members - 1) + fibonacci_recursion(number_members - 2)


print(fibonacci_recursion(10))
'''


def fourth_degree(seq):
    return tuple(map(lambda i: i ** 4, seq))


def sum_numbers(func, seq):
    tmp_seq = func(seq)
    return tuple(sum(i) for i in zip(tmp_seq, tmp_seq[1:]))
