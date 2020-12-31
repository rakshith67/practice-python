
i = 0;
while i < 10:
    print("is is now {}".format(i))
    i += 1


available_exits = ["Right", "Left", "Up", "Down"]
chose_exit = ""

while chose_exit not in available_exits:
    chose_exit = input("Please select the direction ")
    if chose_exit.casefold() == "quit":
        print("Game Over")
        break

print("Happy with game over?")
