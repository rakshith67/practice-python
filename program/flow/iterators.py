numbers = "1234567890"

my_iterator = iter(numbers)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

for char in iter(numbers):
    print(char)

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
iterator = iter(my_list)

for string in range(0, len(my_list)):
    item = next(iterator)
    print(item)
