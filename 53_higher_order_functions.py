# 53 (04:35:21​) higher order functions 👑

""" 
    Higher order functions are those that:
    * accept a function as an argument
        OR
    * return a function

    NOTE: in Python, functions are also treated as objects
 """

print("\n--- Example 2 - HOF that accepts function as argument ---")


def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(loud)  # HELLO
hello(quiet)  # hello


print("\n--- Example 2 - HOF that returns a function ---")


# NOTE: dividend / divisor = quotient
# divisor = the number used to divide another number by
def divisor(x):
    def dividend(y):
        return y / x

    return dividend  # function


half = divisor(2)  # returns function: dividend
print("--- half = divisor(2) ---")
print(half(10))  # 5.0
print(half(162))  # 81.0

divide_by_5 = divisor(5)  # returns function: dividend
print("--- divide_by_5 = divisor(5) ---")
print(divide_by_5(100))  # 20.0
print(divide_by_5(75))  # 15.0
