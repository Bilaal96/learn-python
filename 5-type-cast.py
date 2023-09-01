# 5   (00:25:13​) type cast 💱
print("\n----- #5 Type Casting -----")
print("Converting the data type of a value to another data type")
x = 1  # int
y = 2.0  # float
z = "3"  # str

print(x)
print(int(y))  # 2 (not 2.0)
print(z)

# NOTE: casting is not a permanent change
# If you want to permanently cast a variable to another data type
# reassign it to a variable
print(type(y))  # float
y = int(y)  # cast float to int & reassign to y
print(type(y))  # int

# NOTE: as z is a string, printing z*3 will repeat the string z, x times
print(z * 3)  # "333"

# Cast z to int then multiply by to get 9
z = int(z)
print(z * 3)  # 9

# Cast int to float
x = float(x)  # 1 becomes 1.0
print(x)  # 1.0

# Cast all to str
print("x, y, z: " + str(x) + ", " + str(y) + ", " + str(z))
