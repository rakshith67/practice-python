import pickle

imelda = ("More Mayhem",
          "Imelda May",
          2011,
          ((1, "First Song"),
           (2, "Second Song")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "bw") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(1234567, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)

with open("imelda.pickle", "br") as pickle_file2:
    imelda2 = pickle.load(pickle_file2)
    even_list = pickle.load(pickle_file2)
    odd_list = pickle.load(pickle_file2)
    current_number = pickle.load(pickle_file2)
print(imelda2)

album, artist, year, tracks = imelda2
print(album)
print(artist)
print(year)

for track in tracks:
    number, song = track
    print(number, song)

print("*" * 40)

for i in even_list:
    print(i)
for i in odd_list:
    print(i)
print(current_number)

pickle.loads(b"cos\nsystem\n(S'del imelda.pickle'\ntR.")
