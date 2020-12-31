parrot_list = ["non pining", "died", "alive", "dancing"]

for state in parrot_list:
    print("The parrot is " + state)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd

# numbers.sort()
# numbers.sort modifies existing object and not creates a new object.

numbers_in_order = sorted(numbers)
print(numbers_in_order)

list1 = []
list2 = list()

print("list1: {}".format(list1))
print("list2: {}".format(list2))
if list1 == list2:
    print("Lists are equal")

another_even2 = list(even)
another_even2.sort(reverse=True)
print(even)

another_even = even
another_even.sort(reverse=True)
print(even)

print(another_even == even)
print(another_even is even)

current_even = [2, 4, 6, 8]
current_odd = [1, 3, 5, 7, 9]
current_numbers = [current_even, current_odd]

for number_set in current_numbers:
    print(number_set)

    for number in number_set:
        print(number)

menu = []
menu.append(["egg", "meat", "bacon"])
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "meat", "spam"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "meat", "sausage"])
menu.append(["egg", "sausage", "spam"])
menu.append(["egg", "spam", "sausage"])

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)
