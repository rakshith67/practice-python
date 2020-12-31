my_list = list(range(10))
print(my_list)

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))
print(even)
print(odd)

numbers = range(0, 10)
print(numbers)
print(numbers.index(3))

odd = range(1, 10000, 2)
print(odd)
print(odd[985])

print(numbers)
my_range = numbers[::2]
print(my_range)
print(my_range.index(4))

decimals = range(0, 100)
print(decimals)

my_decimals = decimals[3:40:3]
print(my_decimals)

for i in my_decimals:
    print(i)

print('=' * 40)

for i in range(3, 40, 3):
    print(i)

print(my_decimals == range(3, 40, 3))

print('=' * 50)

current_range = range(0, 100)

for i in current_range[::-2]:
    print(i)

print('=' * 50)

for i in range(99, 0, -2):
    print(i)

print('=' * 50)

print(range(0, 100)[::-2] == range(99, 0, -2))

for i in range(0, 100, -2):
    print(i)


