import shelve

# shelve accepts only key as string
with shelve.open("ShelveTest") as fruit:
    fruit["orange"] = "a sweet, citrus fruit"
    fruit["apple"] = "good for making cider"
    fruit["lemon"] = "a sour fruit"
    fruit["lime"] = "a sweet, yellow fruit"
    fruit["grape"] = "a small, bunch fruit"

    print(fruit["apple"])
    print(fruit["lemon"])

bike = shelve.open("Bike")
bike["company"] = "Honda"
bike["colour"] = "red"
bike["model"] = "250 dream"
bike["engine"] = 250

bike["engine"] = 350

print(bike["engine"])
print(bike["company"])

for value in bike.values():
    print(value)
print(bike.values())

for item in bike.items():
    print(item)
print(bike.items())

bike.close()

blt = ["bacon", "lettuce"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "bread", "milk"]
soup = ["soup"]
pasta = ["pasta", "cheese"]

with shelve.open("Recipes", writeback=True) as recipes:
    recipes["blt"] = blt
    recipes["beans_on_toast"] = beans_on_toast
    recipes["scrambled_eggs"] = scrambled_eggs
    recipes["soup"] = soup
    recipes["pasta"] = pasta

    recipes["pasta"].append("tomato")

    temp_list = recipes["soup"]
    temp_list.append("tomato")
    recipes["soup"] = temp_list

    recipes["beans_on_toast"] = beans_on_toast
    recipes.sync()
    beans_on_toast.append("tomato")

    for snack in recipes:
        print(snack, recipes[snack])
