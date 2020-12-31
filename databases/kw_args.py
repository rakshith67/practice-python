
def print_backwards(*args, **kwargs):
    end_character = kwargs.pop("end", "\n")
    sep_character = kwargs.pop("sep", "\n")
    for word in args[::-1]:
        print(word[:0:-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)


with open("backwards.txt", 'w') as file:
    print_backwards("Hello", "Earth", "how", "are", "you", file=file)

print()
print("Hello", "Earth", "how", "are", "you", end="\n", sep="|")
print_backwards("Hello", "Earth", "how", "are", "you", end="\n", sep="|")
