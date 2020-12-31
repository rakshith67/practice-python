import os


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(s)
        for file in files:
            current_dir = os.path.join(d, file)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + file)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1

    tab_stop = 0
    if os.path.exists(s):
        print("Directory Listings of " + s)
        dir_list(s)
    else:
        print(s + " does not exists")


def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number-1)


for i in range(0, 101):
    print("{}: {}".format(i, factorial(i)))
list_directories('.')
