# 49 (04:19:12) objects as arguments 🏍️

""" 
    Functions may accept objects (instances of a class) as args
    
    The type of object received as arg may be limited by the logic 
    of the function 
    e.g. with the change_color function below, you can only change the color
    of a vehicle (or technically any other object) if it has a "color" property

 """


class Car:
    color = None


class Motorcycle:
    color = None


# vehicle -> instance of some Vehicle class (e.g. Car)
# color -> new color to apply to vehicle
def change_color(vehicle, color):
    vehicle.color = color


# Examples with Car
car1 = Car()
car2 = Car()
car3 = Car()

change_color(car1, "red")
change_color(car2, "white")
change_color(car3, "blue")

print("car1.color:", car1.color)  # car1.color: red
print("car2.color:", car2.color)  # car2.color: white
print("car3.color:", car3.color)  # car3.color: blue


# Example with Motorcycle
bike1 = Motorcycle()
change_color(bike1, "black")
print("bike1.color:", bike1.color)  # bike1.color: black
