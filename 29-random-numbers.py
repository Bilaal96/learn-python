# 29 (02:33:22​) random numbers 🎲
# Exploring useful methods of the random module
import random

print("\n----- #29 Creating Pseudo-Random Numbers -----")
# Simulate dice roll - gen number from 1-6
print("\n# random.randint()")
x = random.randint(1, 6)
print(x)  # A random number from 1-6

# Gen random floating point number from 0-1
print("\n# random.random()")
y = random.random()
print(y)

# Randomly choose element in a list
print("\n# random.choice()")
myList = ["rock", "paper", "scissors"]
z = random.choice(myList)
print(z)

# Shuffle a collection (such as a list)
print("\n# random.shuffle()")
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
