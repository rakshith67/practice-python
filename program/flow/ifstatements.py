name = input("Please enter your name: ")
age = int(input("Hpw old are you {0}? ".format(name)))
print(age)

if age < 18:
    print("You are elgible to vote")
    print("Please put a X in the box")
elif age == 900:
    print("Sorry, you died")
else:
    print("Please comeback in {0} years".format(18 - age))
