# 54 (04:41:06​) lambda λ

""" 
    Functions written in one line using 'lambda' keyword

    Syntax:
    lambda parameters: expression

    Accepts any number of arguments
    Evaluates & returns the result of an expression
    i.e. it returns a single value

    Useful if needed for one use / a short period of time 
    before "throwing away" the function

    The example below will replicate this function as a lambda function

    # multiplies x by 2
    def double(x):
        return x * 2
 """

print("--- Example 1 - double(x) ---")
double = lambda x: x * 2
print(double(5))  # 10

print("\n--- Example 2 - multiply(x, y) ---")
multiply = lambda x, y: x * y
print(multiply(5, 3))  # 15

# NOTE: Calling multiply with a single arg results in the following
# error as it expects 2 arguments

# print(multiply(5))
# TypeError: <lambda>() missing 1 required positional argument: 'y'

print("\n--- Example 3 - add(x, y, z) ---")
add = lambda x, y, z: x + y + z
print(add(5, 6, 7))  # 18

print("\n--- Example 3 - full_name(first_name, last_name) ---")
full_name = lambda first_name, last_name: first_name + " " + last_name
print(full_name("Peter", "Parker"))  # Peter Parker

print("\n--- Example 4 - age_check(age) ---")
""" 
    Using if-else condition with a lambda function

    lambda x: <truthy_return_value> if <condition> else <falsy_return_value>
 """
age_check = lambda age: True if age >= 18 else False

print(age_check(18))  # True
print(age_check(17))  # False
