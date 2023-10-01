# 46 (04:04:14​) method chaining ⛓️

# Used to call multiple methods sequentially
# Each call performs an action on the same object and returns itself


class Car:
    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

print("--- With method chaining ---")
car.turn_on().drive().brake().turn_off()

""" 
    Can format the above like so for readability:

    car.turn_on()\
        .drive()\
        .brake()\
        .turn_off()

    NOTE: \ is known as a "line continuation character"
 """

# Same as
print("\n--- Without method chaining ---")
car.turn_on()
car.drive()
car.brake()
car.turn_off()
