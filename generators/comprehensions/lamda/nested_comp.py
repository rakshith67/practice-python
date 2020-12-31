burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "egg", "beans"]

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, i * j)


times = [[(i, i * j) for i in range(1, 11)] for j in range(1, 11)]
print(times)

for x, y in [(i, j) for i in range(1, 11) for j in range(1, 11)]:
    print("{} times {} is {}".format(x, y, x * y))
