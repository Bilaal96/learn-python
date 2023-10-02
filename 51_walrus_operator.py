# 51 (04:27:38) walrus operator 🦦

# :=   <--  assignment expression AKA walrus operator
# new to Python 3.8
# assigns values to variables as part of a larger expression

""" 
    happy = True
    print(happy) # True 

 """

print("--- Example 1 ---")

# equivalent to above:
# Assigns True to happy, then prints happy
print(happy := True)  # True

# happy is an accessible variable
print(happy)  # True


print("\n--- Example 2 ---")
""" 
    foods = list()

    while True:
        food = input("What food do you like?: ")
        if food == "quit":
            break
        foods.append(food)

    print(foods) 
 """

# Shorten above code with walrus operator
foods = list()

# Evaluates right-side (expression) before assigning the result to foods
# If input != "quit" --> food = True
# If input == "quit" --> food = False --> exit condition


""" 
    (food := input("What food do you like?: ")) != "quit"

    The assignment expression (left) is wrapped in brackets so that the input
    value is stored in the 'food' variable

    Then the rest of the expression is evaluated:
    food != "quit"
 """

while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

print(foods)
# e.g. banana, apple, orange, ice cream, pizza, chips
