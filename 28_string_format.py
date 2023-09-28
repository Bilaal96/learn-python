# 28 (02:21:17​) string format 💬
print("\n----- #28 str.format() -----")

# optional method (alternative to print) that gives users more control when displaying output

animal = "cow"
item = "moon"

# String concatenation
print("\n# String concatenation")
print("The " + animal + " jumped over the " + item)


# Format string literal
print("\n# Format string literal")
print(f"The {animal} jumped over the {item}")

# str.format() with string values as arguments
# NOTE: the curly braces are known as format fields
# -- they're placeholders for a value/variable
# -- the args of format() are passed to the respective format field
print("\n### str.format()")
print("# with value as arg")
print("The {} jumped over the {}".format("cow", "moon"))

# str.format() with string variables as arguments
print("\n# with variable as arg")
print("The {} jumped over the {}".format(item, animal))
print("The {} jumped over the {}".format(animal, item))

print("\n# with positional arguments")
print("The {1} jumped over the {0}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))

# NOTE: for this example, the above variables do not have to be defined
print("\n# with keyword arguments")
print("The {animal} jumped over the {item}".format(animal="horse", item="skyscraper"))

# NOTE: the positional / keyword arguments can be reused throughout the string by referring to the position index / keyword arg (respectively)
print("\n# reusing positional / keyword arguments")

print("The {0} jumped over the {1} {0}".format(animal, item))
# The cow jumped over the moon cow

print(
    "The {animal} jumped over the {item} {animal}".format(
        animal="horse", item="skyscraper"
    )
)
# The horse jumped over the skyscraper horse

print("\n# applying .format() to a string variable")
text = "The {} jumped over the {}"
print(text.format(animal, item))
# The cow jumped over the moon

print("\n# applying padding to a string using .format()")

name = "Bilaal"
print("Hello my name is {}".format(name))

print("\n -- apply padding to format value")
# allocate 10 spaces of padding to name
# -- default - align value to left of padding
alignment = "<<< Align value {} padding using {}"
leftAlign = alignment.format("left of", "< or leave as default :<padding>")
rightAlign = alignment.format("right of", ">")
centerAlign = alignment.format("in center of", "^")

print("Hello my name is {:10}. Nice to meet you!".format(name), leftAlign)
# -- manually align value to left of padding
print("Hello my name is {:<10}. Nice to meet you!".format(name), leftAlign)
# -- align value to right of padding
print("Hello my name is {:>10}. Nice to meet you!".format(name), rightAlign)
# -- align value in center of padding - i.e. 5 spaces each side
print("Hello my name is {:^10}. Nice to meet you!".format(name), centerAlign)

# To use a positional or keyword arg, simply prefix the padding with the position index or the keyword arg
print(
    "Hello my name is {0:>10} {1:<10} . Nice to meet you!".format("Benjamin", "Button"),
    centerAlign,
)
print(
    "Hello my name is {custom_name:^10}. Nice to meet you!".format(custom_name="Bob"),
    centerAlign,
)


print("\n### Format numbers")
number = 3.14159

# Display a number rounded to 2 decimal places
# :2f --> a floating point number with precision of 2 decimal places
print("The number pi to 2 decimal places: {:.2f}".format(number))  # 3.14

# NOTE: formatting numbers in this manner will round the number to 3 sig. fig.
# 3.14159 to 3 sig. fig. is rounded to 3.142
print("The number pi to 3 decimal places: {:.3f}".format(number))  # 3.142

# :, --> Add comma to 1000th places
number = 1000
print("The number is: {:,}".format(number))  # 1000 => 1,000

# :b --> Display number in binary format
print("The number is: {:b}".format(number))  # 1111101000

# :o --> Display number in octal format
print("The number is: {:o}".format(number))  # 1750

# :x (lowercase x) --> Display number in lowercase hexadecimal format
print("The number is: {:x}".format(number))  # 3e8
# :X (uppercase x) --> Display number in uppercase hexadecimal format
print("The number is: {:X}".format(number))  # 3E8

# :e (lowercase e) --> Display number in lowercase scientific notation
print("The number is: {:e}".format(number))  # 1.000000e+03
# :E (uppercase e) --> Display number in uppercase scientific notation
print("The number is: {:E}".format(number))  # 1.000000E+03
