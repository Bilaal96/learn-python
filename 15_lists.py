# 15 (01:21:06​) lists / arrays 🧾
print("\n----- #15 Lists -----")

food = ["pizza", "hamburger", "spaghetti"]

print(food)  # ['pizza', 'hamburger', 'spaghetti']


print("\n### Access list elements by index")
print(food[0])
print(food[1])
print(food[2])
# UNCOMMENT LINE BELOW TO TEST
# print(food[10]) # IndexError: list index out of range


print("\n### Reassignment to list index")
# NOTE: elements can be of varying types
food[0] = 1
food[1] = True
food[2] = None
# food[3] = None # IndexError: list index out of range
print(food)
print()


print("\n### Iterate and print each element in a list")
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
food[2] = "sushi"  # replace hotdog with sushi

for item in food:
    print(item)


print("\n### List Methods")

food.append("ice cream")  # returns None
print(food)  # ['pizza', 'hamburger', 'sushi', 'spaghetti', 'pudding', 'ice cream']

# Remove first occurrence of value / ValueError if value doesn't exist
food.remove("pudding")
# food.remove("test") # ValueError
print(food)  # ['pizza', 'hamburger', 'sushi', 'spaghetti', 'ice cream']

# Remove & return last element in the list
# Raises IndexError if list is empty or index is out of range.
print(food.pop())  # "ice cream"

# Insert at given index
food.insert(0, "cake")  # returns None
print(food)  # ['cake', 'pizza', 'hamburger', 'sushi', 'spaghetti']

# Sort list alphabetically
food.sort()  # returns None
print(food)  # ['cake', 'hamburger', 'pizza', 'spaghetti', 'sushi']

# Clear all items from list
food.clear()  # returns None
print(food)  # []
