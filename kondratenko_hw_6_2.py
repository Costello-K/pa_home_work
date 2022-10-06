# Exercise 1
# Implement a function which receives a string and replaces all " symbols with
# ' and vise versa. The function should return modified string.
# Usage of any replacing string functions is prohibited.
import string


def change_text(text: str):
    if not isinstance(text, str):
        raise TypeError('Wrong type: String only')

    res = []

    for i in text:
        if i == '\'':
            i = '"'
        elif i == '"':
            i = '\''
        res.append(i)

    return ''.join(res)


print(change_text("Ent'er text to cha\"ge"))

# • Exercise 2
# Write is_palindrome function that checks whether a string is a palindrome or not.
# Returns 'True' if it is palindrome, else 'False’.
# To check your implementation you can use strings from here
# (https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
# Note:
# - Usage of any reversing functions is prohibited
# - The function has to ignore special characters, whitespaces and different cases
# - Raise ValueError in case of wrong data type


def is_palindrome(arg: str | int):
    if not isinstance(arg, str | int):
        raise TypeError('Wrong type: Integer or String only')

    s = str(arg)
    half_len = len(s) // 2

    return True if s[:half_len] == s[:-half_len - 1:-1] else False


print(is_palindrome('rty/7/ytr'))

    # V-2
    # i = 0
    # while i < half_len:
    #     if s[i] != s[-i - 1]:
    #         return False
    #     i += 1
    # else:
    #     return True

# • Exercise 3
# Implement a function which works the same as str.split.
# Note:
# - Usage of str.split method is prohibited
# - Raise ValueError in case of wrong data type


def func_split(text: str, sep=' '):
    if not isinstance(text, str):
        raise TypeError('Wrong type: String only')

    res = []

    w = []
    for i in text:
        if i != sep:
            w.append(i)
        else:
            res.append(''.join(w))
            w.clear()
    res.append(''.join(w))

    return res


print(func_split('pythoniscool,isnscool,isnscool,isn', ','))
print('pythoniscool,isnscool,isnscool,isn'.split(','))
print(func_split('pythoniscool isnscool isnscool isn'))
print('pythoniscool isnscool isnscool isn'.split())
print(func_split('pythoniscool,isnscool,isnscool,isn', 'n'))
print('pythoniscool,isnscool,isnscool,isn'.split('n'))
print(func_split('pythoniscool,isnscool,isnscool,isn', 'p'))
print('pythoniscool,isnscool,isnscool,isn'.split('p'))

# Exercise 4
# Implement a function split_by_index(string: str, indexes: List[int]) -> List[str]
# which splits the string by indexes specified in indexes.
# Only positive index, larger than previous in list is considered valid. Invalid indexes must be ignored.
# Examples:
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
# >>> split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18])
# ["python", "is", "cool", ",", "isn't", "it?"]
# >>> split_by_index("no luck", [42])
# ["no luck"]


def split_by_index(text: str, indexes: list[int]):
    res = []

    i = 0
    for ind in indexes:
        if not isinstance(ind, int):
            continue
        elif i < ind:
            res.append(text[i:ind])
            i = ind
    if indexes[-1] < len(text):
        res.append(text[i:])

    return res


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("pythoniscool,isn'tit?", [6, 8, 8, -4, 0, "u", 12, 13, 18]))
print(split_by_index("no luck", [42]))

# • Exercise 5
# Implement a function get_digits(args: int) -> Tuple[int] which receives arbitrary
# amount of arguments and returns a tuple of digits of given integers.
# Example:
# >>> split_by_index(8717, 82911, 99)
# (8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)


def get_digits(*args: int):

    return tuple(map(int, ''.join(map(str, args))))


print(get_digits(8717, 82911, 99))

# Exercise 6
# Implement a function get_longest_word(s: str) -> str which returns the longest word
# in the given string. The word can contain any symbols except
# whitespaces (`,\n,\t and so on). If there are multiple longest words in the string
# with a same length return the word that occurs first.
# Example:
# get_longest_word('Python is simple and effective!’)
# #output: 'effective!’
# get_longest_word('Any pythonista like namespaces a lot.’)
# #output: 'pythonista’
# Note:
# - Raise ValueError in case of wrong data type
# - Usage of 're' library is prohibited


def get_longest_word(s: str):
    punctuation = [('\n', '\\n'), ('\t', '\\t'), ('\v', '\\v'), ('\r', '\\r'),
                   ('\f', '\\f'), ('\b', '\\b'), ('\a', '\\a')]
    for i, k in punctuation:
        while i in s:
            s = s.replace(i, k)

    return max(''.join(list(s)).split(), key=len)

print(get_longest_word('Python is si\nm\npl\te and effe\nctive!'))


# • Exercise 7
# Implement a function foo(List[int]) -> List[int] which, given a list of integers,
# returns a new or modified list in which every element at index i of the
# new list is the product of all the numbers in the original array except the one at i.
# Example:
# foo([1, 2, 3, 4, 5])
# [120, 60, 40, 30, 24]
# foo([3, 2, 1])
# [2, 3, 6]


def foo(data: list[int]):
    for i in data:
        if not isinstance(i, int):
            raise TypeError('Wrong type: Integer only')

    res = []

    for k in data:
        product = 1
        for i in data:
            if i != k:
                product *= i
        res.append(product)

    return res


print(foo([1, 2, 3, 4, 5]))

# Exercise 8
# Implement a function which takes a list of elements and returns a list of tuples containing pairs of this elements.
# Pairs should be formed as in the example. If there is only one element in the list return None instead.
# Using zip() is prohibited.
# Examples:
# >>> get_pairs([1, 2, 3, 8, 9])
# [(1, 2), (2, 3), (3, 8), (8, 9)]
# >>> get_pairs(['need', 'to', 'sleep', 'more’])
# [('need', 'to'), ('to', 'sleep'), ('sleep', 'more’)]
# >>> get_pairs([1])
# None


def get_pairs(data: list):
    if len(data) < 2:
        return None

    res = []

    i = 0
    while (i := i + 1) < len(data):
        res.append((data[i - 1], data[i]))

    return res


print(get_pairs(['need', 'to', 'sleep', 'more']))

# • Exercise 9
# For a positive integer n calculate the result value, which is equal to the sum of the odd numbers of n.
# Example,
# n = 1234 result = 4
# n = 246 result = 0
# Write it as function.
# Note:
# - Raise TypeError in case of wrong data type or negative integer;
# - Use of 'functools' module is prohibited, you just need simple for loop


def sum_odd_digits(number: int):
    if not isinstance(number, int):
        raise TypeError('Wrong type: Integer only')
    if number < 0:
        raise ValueError('Wrong value: Integer must be greater than zero')

    return sum(i for i in map(int, str(number)) if i % 2)


print(sum_odd_digits(1234))

# Exercise 10
# Create a function sum_binary_1 that for a positive integer n calculates the result value,
# which is equal to the sum of the “1” in the binary representation of n
# otherwise, returns None.
# Example,
# n = 14 = 1110 result = 3
# n = 128 = 10000000 result = 1


def sum_binary_1(number: int):
    if not isinstance(number, int):
        raise TypeError('Wrong type: Integer only')
    if number < 0:
        raise ValueError('Wrong value: Integer must be greater than zero')

    return bin(number)[2:].count('1') or None


print(sum_binary_1(14))

# • Exercise 11
# Write a function fibonacci_loop(seq: list), which accepts a list of values and
# prints out values in one line on these conditions:
# - floating point numbers should be ignored
# - string values should stop the iteration
# - loop control statements should be used
# Example:
# >>> fibonacci_loop([0, 1, 1.1, 1, 2, 99.9, 3, 0.0, 5, 8, "stop", 13, 21, 34])
# 0 1 1 2 3 5 8


def fibonacci_loop(seq: list):
    res = []

    for i in seq:
        if isinstance(i, str):
            break
        elif isinstance(i, int):
            if sum(res[-2:]) == i or len(res) == i or not i and not res:
                res.append(i)

    return ' '.join(map(str, res)) if res else 'Fibonacci loop not found'


print(fibonacci_loop([0, 6, 1, 1.1, 1, 1, 2, 99.9, 1, 6, 3, 0.0, 5, 8, 8, 8, "stop", 13, 21, 34]))
