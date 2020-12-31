print(__file__)

numbers = [1, 2, 3, 4, 5, 6, 7]
number = int(input("Pleas enter a number I will tell its square "))
squares = [number ** 2 for number in range(1, 7)]
index_pos = numbers.index(number)  # using for loop the number will be always 6
# as it is used in for loop variable (loop controlled variable)
print(squares[index_pos])
print(squares)

words = "What have the romans done for us"
words = [word.upper() for word in words.split(' ')]
print(words)
