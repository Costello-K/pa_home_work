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
    for k in range(1, seq[1] - seq[0]):
        if min((i + 1) ** k == seq[i] for i in range(len(seq))):
            return True

    return False


def next_member_degree_progression(seq):
    for k in range(1, seq[1] - seq[0]):
        if min((i + 1) ** k == seq[i] for i in range(3)):
            return (len(seq) + 1) ** k
