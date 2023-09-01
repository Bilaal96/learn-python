import re  # regex module

# 13 (01:13:04​) nested loops ➿
print("\n----- #13 Nested Loops -----")

print("Let's create a 2 plain with a symbol/character of your choice!\n")

char = input("What character should we use?: ")
# validate input char
while not len(char) == 1 or re.match("^[\s]$", char):
    # Ensure char is anything except whitespace
    if re.match("^[\s]$", char):
        print("\nWhoops! Please enter any character except whitespace...")
        char = input("What character should we use?: ")

    # Ensure char length == 1
    if len(char) > 1:
        print("\nWhoops! You can only enter one character...")
        char = input("What character should we use?: ")
    elif len(char) == 0:
        print("\nWhoops! You must enter one character...")
        char = input("What character should we use?: ")


rows = int(input("How many rows shall we print?: "))
# validate input rows
while not isinstance(rows, int) or rows < 1:
    # rows is int?
    if not isinstance(rows, int):
        print("\nWhoops! Rows must be an integer...")
        rows = int(input("How many rows shall we print?: "))

    # rows is > 0?
    if rows < 1:
        print("\nWhoops! We need a number greater than zero...")
        rows = int(input("How many rows shall we print?: "))


# validate input: columns
columns = int(float(input("How many columns shall we print?: ")))
while not isinstance(columns, int) or columns < 1:
    # columns is int?
    if not isinstance(columns, int):
        print("\nWhoops! Columns must be an integer...")
        columns = int(input("How many columns shall we print?: "))

    # columns is > 0?
    if columns < 1:
        print("\nWhoops! We need a number greater than zero...")
        columns = int(input("How many columns shall we print?: "))

# My Working Solution
""" for i in range(rows):
    current_line = ""
    for j in range(columns):
        current_line += char
    print(current_line) """

# Use print(char, end="") to prevent cursor from moving to next line
# i.e. keep printing on the same line
for i in range(rows):
    for j in range(columns):
        print(char, end="")  # print char on the same line, columns times
    print()  # new line
