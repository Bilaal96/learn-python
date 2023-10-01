# 42 (03:48:54​) inheritance 👪

# Where a subclass inherits attributes and methods from the parent class
# A subclass may also override attributes/methods of its parent


# Parent class
class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


# Subclasses - or child classes
# NOTE: how each inherits from its parent and can also have their own unique properties/methods


# Rabbit extends (i.e. inherits from) Animal
class Rabbit(Animal):
    def run(self):
        print("This Rabbit is running")


# Fish extends (i.e. inherits from) Animal
class Fish(Animal):
    def swim(self):
        print("This Fish is swimming")


# Hawk extends (i.e. inherits from) Animal
class Hawk(Animal):
    def fly(self):
        print("This Hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print("--- Rabbit ---")
print(rabbit.alive)  # True
rabbit.run()  # This Rabbit is running

print("\n--- Fish ---")
fish.eat()  # This animal is eating
fish.swim()  # This Fish is swimming

print("\n--- Hawk ---")
hawk.sleep()  # This animal is sleeping
hawk.fly()  # This Hawk is flying
