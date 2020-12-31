text = "What have the romans ever done for us"

map_capitals = list(map(str.upper, text))
print(map_capitals)

capitals = [char.upper() for char in text]
print(capitals)

word_capitals = [word.upper() for word in text.split(' ')]
print(word_capitals)

map_word_capitals = list(map(str.upper, text.split(' ')))
print(map_word_capitals)
