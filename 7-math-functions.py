# 7 (00:36:50​) math functions 🧮
import math  # native module

print("\n----- #7 Math Functions -----")

pi = 3.14

# Doesn't require math module
print("# round() - round to nearest int")
print(round(pi))  # 3

print("\n# math.ceil() - round up to nearest int")
print(math.ceil(pi))  # 4

print("\n# math.floor() - round down to nearest int")
print(math.floor(pi))  # 3

# Doesn't require math module
print(
    "\n# abs() - return absolute value of number - i.e. how far away a number is from zero"
)
print(abs(pi))  # 3.14
print(abs(-3.14))  # 3.14
print(abs(-250))  # 250

# Doesn't require math module
print("\n# pow(base, exponent) - raises base by exponent")

print(pow(pi, 2))  # pi squared = 9.8596
# Equivalent to:
print(pi**2)  # pi squared = 9.8596
# NOTE: it returns a float

print("\n# math.sqrt() - returns square-root of given value")
print(math.sqrt(pi))  # 1.772004514666935
print(math.sqrt(81))  # 9.0
# NOTE: it returns a float

# Doesn't require math module
print("\n# max() - returns largest value of all arguments received")

x = 1
y = 2
z = 3

print(max(x, y, z))  # 3 (z)

print("\n# min() - returns smallest value of all arguments received")

print(min(x, y, z))  # 1 (x)
