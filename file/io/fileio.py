file = open("C:\\Users\\rakshim1\\OneDrive - AMDOCS\\Backup Folders\\Documents\\useful data\\TODO-Learning.txt", 'r')

for line in file:
    print(line, end='')

file.close()
print()

with open("demo.txt", 'r') as currentFile:
    for line in currentFile:
        if "array" in line.lower():
            print(line, end='')
print()

with open("demo.txt", 'r') as secondFile:
    line = secondFile.readline()
    while line:
        print(line, end='')
        line = secondFile.readline()
print()

with open("demo.txt", 'r') as thirdFile:
    lines = thirdFile.readlines()
print(lines)

with open("demo.txt", 'r') as fourthFile:
    lines = fourthFile.readlines()
    for line in lines[::-1]:
        print(line, end='')

with open("demo.txt", 'r') as fifthFile:
    lines = fifthFile.read()
    for line in lines[::-1]:
        print(line, end='')
