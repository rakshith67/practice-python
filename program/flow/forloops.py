statement = "9;789.985:879 987,657;983"
separators = ""

for char in statement:
    if not char.isnumeric():
        separators += char

print(separators)

values = "".join(char if char not in separators else " " for char in statement).split()
print(sum(int(value) for value in values))

for i in range(1, 20):
    print("i is now {}".format(i))

for i in range(0, 10, 2):
    print("i is now {}".format(i))

for i in range(10, 0, -2):
    print("i is now {}".format(i))
