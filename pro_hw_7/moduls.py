def geometric_progression_generator(multiplier, limit):
    next_value = multiplier
    while next_value < limit:
        res = yield next_value
        if res:
            return
        next_value *= multiplier


def geometric_progression(multiplier: int, limit: int, max_number_of_iterations: int):
    if not isinstance(sum((multiplier, limit, max_number_of_iterations)), int):
        raise TypeError

    iteration, value = 0, 0
    try:
        seq = geometric_progression_generator(multiplier, limit)
        for k, v in enumerate(seq):
            if k == max_number_of_iterations:
                iteration, value = k, v
                seq.send(True)
        return geometric_progression_generator(multiplier, limit)
    except StopIteration:
        print(f'Error. Sequence has reached iteration {iteration} with value: {value}')


def number_generator(*args: int):
    if len(args) > 3:
        raise ValueError('too many values to unpack (expected 3)')
    if not isinstance(sum(args), int):
        raise TypeError

    start = args[0] if len(args) > 1 else 0
    stop = args[1] or args[0]
    step = args[2] or 1

    i = 0
    while start < stop:
        if not i % step:
            yield start
        i += 1
        start += 1


def prime_numbers(limit: int):
    if not isinstance(limit, int):
        raise TypeError

    i = 1
    while i <= limit:
        if i % 2 and i % 3 and i % 5 and i % 7 or i == 2 or i == 3 or i == 5 or i == 7:
            yield i
        i += 1
