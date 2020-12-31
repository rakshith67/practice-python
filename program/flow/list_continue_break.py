shopping_list = ["Milk", "Bread", "Eggs", "Spam", "Chicken", "Pasta"]

for item in shopping_list:
    if item == "Spam":
        continue

    print("Buy {0}".format(item))

found_at = None
item_to_find = "Spam"

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
print("item found at position {0}".format(index))


