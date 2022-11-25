from math import log


def is_arithmetic_progression(seq):
    difference = seq[1] - seq[0]

    for i in range(len(seq) - 1):
        if difference != seq[i + 1] - seq[i]:
            return False

    return True


def next_member_arithmetic_progression(seq):
    return 2 * seq[-1] - seq[-2]


def is_geometric_progression(seq):
    if not seq[0]:
        return False

    multiplier = seq[1] // seq[0]

    for i in range(len(seq) - 1):
        if multiplier != seq[i + 1] // seq[i]:
            return False

    return True


def next_member_geometric_progression(seq):
    return seq[-1] ** 2 // seq[-2]


def is_degree_progression(seq):
    for k in range(2, seq[1]):
        if is_arithmetic_progression(tuple(round(pow(i, 1/log(seq[1], k)), 3) for i in seq)):
            return True

    return False


def next_member_degree_progression(seq):
    for k in range(2, seq[1]):
        degree = log(seq[1], k)
        if is_arithmetic_progression(tuple(round(pow(i, 1/log(seq[1], k)), 3) for i in seq)):
            return int((pow(seq[-1], 1/degree) + 1) ** degree)

    return None
