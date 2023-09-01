# 6   (00:30:14​) user input ⌨️
print("\n----- #6 User Input -----")

# Prompt user for input and assign input to var "name"
# NOTE: accepted input is always of string data type
name = input("What is your name?: ")
print("Hello " + name)


# NOTE: In order to use numeric input values in arithmetic -> type cast to int/float
age = int(input("What is your age?: "))


def is_able_to_drink(age):
    return 18 - age <= 0


if is_able_to_drink(age):
    print("You can be served at the bar")
else:
    # Cast age back to string to print it
    print(str(age) + "?! You're and underage! Skidaddle")

# Now a ValueError occurs when you pass an input that cannot be cast directly to int
# e.g. alphabetic/non-int string values CANNOT be cast to int
# - int(input("What is your age?: ")) >> "r"
# - ValueError: invalid literal for int() with base 10: 'r'

# e.g. float value as string cannot be cast directly to int
# - int(input("What is your age?: ")) >> 21.7
# - ValueError: invalid literal for int() with base 10: '21.7' <--- is a string

# To indirectly parse a string-float to int
# - 1st parse str to float = float("21.7") => 21.7
# - then float to int = int(21.7) => 21  # always rounds down & truncates the decimal

# Cast input for height to float
height = float(input("How tall are you (in metres)?: "))
print("You are " + str(height) + "m tall")
