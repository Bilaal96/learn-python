# 43 (03:55:30​) multilevel inheritance 👴

# When a derived (child) class inherits form another derived (child) class


# Parent class
class Organism:
    alive = True


# Derived child class / subclass -> inherits from parent
class Animal(Organism):
    def eat(self):
        print("This animal is eating")


# Multilevel inheritance
# Derived Dog class inherits from derived Animal class
class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog = Dog()

print("dog.alive:", str(dog.alive))
dog.eat()
dog.bark()
