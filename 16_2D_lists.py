# 16 (01:26:58​) 2D lists 📜
print("\n----- #16 2D Lists / multi-dimensional - a list of lists -----")

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]
print(
    food
)  # [ ['coffee', 'soda', 'tea'], ['pizza', 'hamburger', 'hotdog'], ['cake', 'ice cream'] ]

print(food[0])  # drinks
print(food[1])  # dinner
print(food[2])  # dessert

print(food[0][1])  # "soda" from drinks list
print(food[1][0])  # "pizza" from dinner list
# print(food[2][2])  # IndexError: list index out of range - desserts only has length of 2
