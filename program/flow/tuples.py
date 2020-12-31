my_tuple = "a", "b", "c"
print(my_tuple)
print("a", "b", "c")
print(("a", "b", "c"))

metallica = "This", "is", "Metallica", 1982
imelda = "This", "Amelda", "may", 2011

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])
print(metallica[3])

# metallica[0] = "updated"

imelda = imelda[0], "Updated", imelda[2], imelda[3]
print(imelda)

metallica2 = ["This", "is", "Metallica", 1982]
print(metallica2)
metallica2[0] = "Updated"
print(metallica2)

# metallica2.append(678)
# current, title, month, year = metallica2
# print(current)

current, title, month, year = imelda
print(current)
print(title)
print(month)
print(year)

players = "1", "2", "3", (
    (1, "1"), (2, "2"), (3, "3")
)

variable1, variable2, variable3, variable4 = players

print(variable1)
print(variable2)
print(variable3)
print(variable4)
