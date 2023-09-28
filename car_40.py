# 40 (03:35:45​) Object Oriented Programming (OOP) 🐍
class Car:
    # constructor fn
    def __init__(self, make, model, year, color):
        # Object attributes - something the object is/has
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Object methods - behaviour/functionality of the object
    def drive(self):
        print("This " + self.model + " is driving")
    
    def stop(self):
        print("This " + self.model + " stopped driving")