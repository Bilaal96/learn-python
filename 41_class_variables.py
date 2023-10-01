# 41 (03:45:06​) class variables 🚗


class Car:
    # Class variables - defined in class, but outside of constructor
    # Available on ALL instances of this class, as well as the constructor itself
    # Has a default assigned value, but can still be modified per instance

    wheels = 4

    def __init__(self, make, model, year, color):
        # Instance variables
        # Available on each instance created from the class
        # Values may be unique per instance
        self.make = make
        self.model = model
        self.year = year
        self.color = color


car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Ford", "Mustang", 2022, "red")

print("--- Access class variables ---")

print("car_1.wheels", str(car_1.wheels))  # 4
car_1.wheels += 2
print("car_1.wheels += 2:", str(car_1.wheels))  # 6

print("car_2.wheels", str(car_2.wheels))  # 4


# Access class variables via the constructor
print("\n--- Access class variables via constructor ---")
print("Car.wheels", str(Car.wheels))  # 4


# All instances created have 4 wheels
print("\n--- Class variables have the same value for each instance ---")
car_3 = Car("Chevy", "Corvette", 2021, "blue")
print("car_3", str(car_3.wheels))  # 2


# Assign value 2 to wheels via constructor
print("\n--- Assign value 2 to .wheels via Car constructor ---")
Car.wheels = 2  # still modifiable
print("Car.wheels", str(Car.wheels))  # 2

# Now all instances will have the updated value of 2 for .wheels
print(
    "\n--- Notice how all instances (old & new) now have updated value of .wheels = 2 ---"
)
car_4 = Car("Ford", "Mustang", 2022, "red")
print("car_2", str(car_2.wheels))  # 2
print("car_3", str(car_3.wheels))  # 2
print("car_4", str(car_4.wheels))  # 2

# NOTE: when the .wheel class variable is modified on the instance (car_1)
# the modification applied to the instance will remain, over that applied to the class itself
print(
    "\n--- The exception being that modifying class variable on an instance will 'override / take precedence over' modification on on the class itself ---"
)
print("car_1", str(car_1.wheels))  # 6
