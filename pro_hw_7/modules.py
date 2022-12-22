def geometric_progression_generator(multiplier, limit):
    next_value = multiplier
    while next_value < limit:
        res = yield next_value
        if res:
            return
        next_value *= multiplier


def geometric_progression(multiplier: int, limit: int, max_number_of_iterations: int):
    if not all(map(lambda p: isinstance(p, int), (multiplier, limit, max_number_of_iterations))):
        raise TypeError

    iteration, value = 0, 0
    try:
        seq = geometric_progression_generator(multiplier, limit)
        for k, v in enumerate(seq):
            if k == max_number_of_iterations:
                iteration, value = k, v
                seq.send('stop')
        return None
    except StopIteration:
        print(f'Error. Sequence has reached iteration {iteration} with value: {value}')


def number_generator(*args: int):
    if not all(map(lambda p: isinstance(p, int), args)):
        raise TypeError

    tmp = slice(*args)
    start, stop, step = tmp.start or 0, \
                        tmp.stop, \
                        tmp.step or 1

    while start < stop and step > 0 or start > stop and step < 0:
        yield start
        start += step


def prime_numbers(limit: int):
    if not isinstance(limit, int):
        raise TypeError

    for i in range(2, limit):
        if i % 2 and i % 3 and i % 5 and i % 7 or i in (2, 3, 5, 7):
            yield i
