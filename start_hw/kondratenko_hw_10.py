import kondratenko_hw_10_modules as sequence_functions
from dict import operation
checkers = ((sequence_functions.is_arithmetic_progression, sequence_functions.next_member_arithmetic_progression),
            (sequence_functions.is_geometric_progression, sequence_functions.next_member_geometric_progression),
            (sequence_functions.is_degree_progression, sequence_functions.next_member_degree_progression)
            )


# 1. Існують такі послідовності чисел:
seq_1 = (0, 2, 4, 6, 8, 10, 12)  # 14
seq_2 = (1, 4, 7, 10, 13)  # 16
seq_3 = (1, 2, 4, 8, 16, 32)  # 64
seq_4 = (1, 3, 9, 27)  # 81
seq_5 = (1, 4, 9, 16, 25)  # 36
seq_6 = (1, 8, 27, 64, 125)  # 216
seq_7 = (1, 6, 25)  # 216
# Реалізуйте програму, яка виведе наступний член цієї послідовності (або подібної до них) на екран.
# Послідовність користувач вводить з клавіатури у вигляді рядка. Наприклад, користувач вводить рядок
# 0,5,10,15,20,25 та відповіддю програми має бути число 30


def next_member_sequence(*args: int):
    if not isinstance(sum(args), int):
        raise TypeError
    if len(args) < 3:
        raise ValueError('Minimum number of sequence members: 3')

    for check, next_sequence in checkers:
        if check(args):
            return next_sequence(args)

    raise ValueError('Sequence is not a progression')


print(next_member_sequence(*seq_1))
print(next_member_sequence(*seq_2))
print(next_member_sequence(*seq_3))
print(next_member_sequence(*seq_4))
print(next_member_sequence(*seq_5))
print(next_member_sequence(*seq_6))
# print(next_member_sequence(*seq_7))


def next_member_sequence_2(actions, *args):
    for action in actions.values():
        for k in range(1, abs(args[2] - args[0])):
            if all(action(args[i], k) == args[i + 1] for i in range(3)):
                return action(args[-1], k)
            if all(action(i + 1, k) == args[i] for i in range(3)):
                return action(len(args) + 1, k)

    raise ValueError('Sequence is not a progression')


print(next_member_sequence_2(operation, *seq_1))
print(next_member_sequence_2(operation, *seq_2))
print(next_member_sequence_2(operation, *seq_3))
print(next_member_sequence_2(operation, *seq_4))
print(next_member_sequence_2(operation, *seq_5))
print(next_member_sequence_2(operation, *seq_6))
# print(next_member_sequence_2(operation, *seq_7))

# 2. Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99.
# Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, vyj;tyyzv яких чисел він є.


def is_palindrome(num):
    text = str(num)
    return True if text == text[::-1] else None


def max_palindrome(start, stop):
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError

    return max((i * j, (i, j)) for i in range(start, stop) for j in range(i, stop) if is_palindrome(i * j))


print(max_palindrome(100, 1000))
