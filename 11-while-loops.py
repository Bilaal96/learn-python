# 11 (01:04:03​) while loops 🔄
print("\n----- #11 While Loops -----")

# Infinite loop - condition is always true
# while 1 == 1:
#     print("Help! I'm stuck in a loop")


# name = input("What is your name?: ")
# name = ""
name = None  # null in python

# # use with name = ""
# while len(name) == 0:

# use with name = None -> is falsy
while not name:
    name = input("What is your name?: ")

print("Hello " + name)
