def odd_numbers():
    current = 1
    while True:
        yield current
        current += 2


def pi_series():
    odd_series = odd_numbers()
    approximation = 0
    while True:
        approximation += (4 / next(odd_series))
        yield approximation
        approximation -= (4 / next(odd_series))
        yield approximation


odds = odd_numbers()
for i in range(100):
    print(next(odds))

approx_pi = pi_series()
for i in range(10):
    print(next(approx_pi))
