# 45 (04:01:49) method overriding 🙅

# Where a subclass overrides a method signature inherited from a parent class
# -- method signature = method name + parameters

# On the child class, simply redefine the same method signature
# from a parent class and implement custom logic/functionality


# An object will check for a method signature more closely associated with itself first
# before relying on a method signature that it may inherit from a parent class
class Animal:
    def eat(self):
        print("This animal is eating")


class Rabbit(Animal):
    # Rabbit.eat() overrides Animal.eat()
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()  # This rabbit is eating a carrot
