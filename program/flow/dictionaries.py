dictionary = {"a": "1",
              "b": "2",
              "c": "3",
              "d": "4",
              "e": "5"}

print(dictionary)
print(dictionary["b"])
dictionary["f"] = "6"
print(dictionary)
dictionary["a"] = "0"
print(dictionary)

del dictionary["a"]
print(dictionary)
dictionary.clear()
print(dictionary)
#
# del dictionary
# print(dictionary)

fruits = {"apple": "good for making cider",
          "orange": "a sweet orange fruit",
          "lemon": "a sour yellow citrus fruit",
          "grape": "small sweet fruit",
          "lime": "a sour green citrus fruit"}

ordered_keys = sorted(list(fruits.keys()))
for key in ordered_keys:
    print(key + " - " + fruits.get(key))

while True:
    key = input("Please enter the fruit name ")
    if key == "quit":
        break
    description = fruits.get(key, "We don't have the fruit {0}".format(key))
    print(description)

fruits_tuple = tuple(fruits.items())
print(fruits_tuple)

for item in fruits_tuple:
    fruit, description = item
    print(fruit + " is " + description)

myList = ["1", "2", "3", "4"]
print(", ".join(myList))

letters = "abcdefghijklmnopqrstuvwxyz"
print(", ".join(letters))

veg = {"cabbage": "green vegetable",
       "brinjal": "blue vegetable"}

veg.update(fruits)
print(veg)

copy_dictionary = veg.copy()
copy_dictionary.update(fruits)
print(copy_dictionary)
