import functools


def calc_values(x, y: int):
    return x + y


numbers = [1, 2, 3, 4, 5, 6]
result = functools.reduce(calc_values, numbers)
print(result)
