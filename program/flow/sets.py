farm_animals = {"cow", "sheep", "goat"}
print(farm_animals)

for farm_animal in farm_animals:
    print(farm_animal)

wild_animals = set(["lion", "tiger", "cheetah", "hyena"])
print(wild_animals)

for animal in wild_animals:
    print(animal)

wild_animals.add("Jaguar")
print(wild_animals)

empty_set = set()
empty_set2 = {}
empty_set.add("add")

even = set(range(0, 40, 2))
print(even)
print(len(even))

squares_tuple = (1, 4, 9, 16, 25, 36)
squares = set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(even.intersection(squares))
print(even & squares)

print("even - squares")
print(sorted(even - squares))
print(sorted(even.difference(squares)))

print("squares - even")
print(sorted(squares - even))
print(sorted(squares.difference(even)))

print("symmetric even - squares")
print(even.symmetric_difference(squares))

print("symmetric squares - even")
print(squares.symmetric_difference(even))

even.difference_update(squares)
print(even)

squares.remove(9)
squares.discard(25)
squares.discard(10)
#squares.remove(10)

subset = {2, 6, 8}

if subset.issubset(even):
    print("subset is a subset of even")

if even.issuperset(subset):
    print("even is superset of subset")
