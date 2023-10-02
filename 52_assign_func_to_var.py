# 52 (04:31:45​) functions to variables 📛
def hello():
    print("Hello")


# Print the function without invoking it
# This displays the memory address of the function
print("hello fn:\n" + str(hello))
# <function hello at 0x000001B0CEAB04A0>

# Assign memory address of function 'hello' to variable 'hi'
# Now 'hi' points to the memory address of the 'hello' function
hi = hello

# Also prints the memory address of 'hello'
print("\nhi variable (points to hello fn):\n" + str(hi))
# <function hello at 0x000001DE6FDB04A0>

# Invokes hello()
print("\n--- Invoke hello() ---")
hello()

print("\n--- Invoke hi() ---")
hi()

print("\n--- Assign existing function (print) to variable ---")
say = print

say("Whoa! I can't believe this works! :O")
