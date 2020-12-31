cities = ["Hyderabad", "Pune", "Bangalore", "Chennai", "Mumbai", "Delhi", "Kolkata"]

with open("cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

currentCities = []
with open("cities.txt", 'r') as readFile:
    for line in readFile:
        currentCities.append(line.strip("\n"))
print(currentCities)
for city in currentCities:
    print(city)

imelda = "More mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Favourite Song")
)
with open("imelda.txt", 'w') as imelda_file:
    print(imelda, file=imelda_file)

with open("imelda.txt", 'r') as imelda_file_read:
    contents = imelda_file_read.readline()

imelda_contents = eval(contents)
title, artist, year, tracks = imelda_contents
print(title)
print(artist)
print(year)
print(tracks)

with open("tables.txt", 'w') as tables_file:
    for i in range(1, 13):
        for j in range(1, 13):
            print("{0:>2} times {1:>2} is {2:>3}".format(i, j, i*j), file=tables_file)
        print("*" * 40, file=tables_file)
