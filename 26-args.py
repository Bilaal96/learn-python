# 26 (02:13:23​) *args 📦
print("\n----- #26 *args -----")

# - *args - a function parameter that allows you to pass a varying number of arguments to a function
# - *args accumulates the arguments within a tuple


# REMEMBER: Tuples are immutable
def printTuple(*args):
    print("values:", args, type(args))


printTuple("Hello", "world")


# REMEMBER: Lists are mutable
def printList(*args):
    stuff = list(args)  # cast tuple to list to modify it
    stuff.append("!")
    print("values:", stuff, type(stuff))


printList("Hello", "world")


def add(*numbers):  # can name *args whatever you want
    total = 0
    for num in numbers:
        total += num
    return total


print(add(3, 5, 7))  # 15
print(add(3, 5, 7, 9))  # 24
print(add(3, 5, 7, 9, 11))  # 35
