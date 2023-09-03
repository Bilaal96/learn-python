# 24 (02:07:09​) nested function calls 🖇️
print("\n----- #24 Nested Function Calls -----")

# i.e. passing a function the invocation of another a function as argument
# outer_func(nested_func())
# The innermost function is evaluated first --> in this case nested_func()
# The return value of nested_func() is passed as an argument to outer_func()
# Then outer_func() is evaluated

""" num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num) # Round a number to a given precision in decimal digits. The return value is an integer if ndigits is omitted or None
print(num)
 """

# Above is equivalent to:
print(round(abs(float(input("Enter a whole positive number: ")))))
