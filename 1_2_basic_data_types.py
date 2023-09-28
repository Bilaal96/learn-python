# 1   (00:00:00)​ Python tutorial for beginners 🐍
print("----- #1 Python tutorial for beginners -----")
print("--- strings ---")
print("Hello World")

# 2   (00:05:57​) variables ✘
print("\n----- #2 Basic Variables / Data Types -----")

name = "Bro"

print("Hello " + name)
print(type(name))  # retrieve type of var

first_name = "Bro"
last_name = "Code"
full_name = first_name + " " + last_name
print("Hello " + full_name)

print("\n--- integer ---")
age = 21
age = age + 1
age += 1
print(age)
print(type(age))

# Cannot do maths with string
strAge = "21"
# strAge += 1 #! TypeError: can only concatenate str (not "int") to str

#! Attempt to print string concatenated with int age fails
# print("Your age is: " + age) #! TypeError: can only concatenate str (not "int") to str

# Type cast int age to str
print("Your age is: " + str(age))

print("\n--- float ---")
height = 250.5  # in cm

# height: 250.5cm <class 'float'>
print("height: " + str(height) + "cm " + str(type(height)))

print("\n--- boolean ---")
human = True
print("is human: " + str(human) + " " + str(type(human)))

ape = False
print("is ape: " + str(ape) + " " + str(type(ape)))
