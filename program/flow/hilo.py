
low = 1
highest = 1000

guess = 1
guesses = 0

while low != highest:
    guess = low + (-low + highest)//2
    print("\tGuessing between {0} and {1}".format(low, highest))
    high_low = input("Guess is {0} Is it h, l or c ".format(guess)).casefold()
    if high_low == 'h':
        low = guess + 1
    elif high_low == 'l':
        highest = guess - 1
    else:
        break
    guesses += 1
else:
    print("You guessed the number {0}".format(low))
    print("Guessed Correct, guessed in {0} guesses".format(guesses))







