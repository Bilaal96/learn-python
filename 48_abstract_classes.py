# 48 (04:12:09​) abstract classes 👻

# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract methods = a method that has a declaration but does not have an implementation

# Abstract class - an idea / template / ghost class to inherit from, or base subclasses on

""" 
    Imagine we're creating a racing video game and we want to create 
    instances of the different types of vehicles (e.g. Car, Motorcycle)

    We don't want to extend the Vehicle class because it is too generic
    We should instead extend Car / Motorcycle

    To signify that Vehicle should not be used to create objects/instances
    we can make it an abstract class

    This involves importing the following from the abc (abstract base class) 
    module:
        - ABC -> Abstract Base Class
        - abstractmethod -> decorator to mark a method as an abstractmethod
            - i.e. a method declaration, without any implementation   

    To make Vehicle an abstract class, simply:
        - extend ABC 
        - Create one or more abstract method(s) - i.e. those without implementation - and mark them with the 
        @abstractmethod decorator

 """

# abc - acronym for = Abstract Base Class
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


""" 
    Classes that extend from the abstract Vehicle class must override 
    its abstract method(s) - i.e. Vehicle.go()

    NOTE: when you don't override the abstract method(s) an error is thrown
    e.g.:
        class Car(Vehicle):
            # missing go() override
            pass

        # Results in:
        TypeError: Can't instantiate abstract class Car with abstract method go

    This is a good form of "checks and balances" - i.e. to be sure that your 
    child classes are not missing any implementation of methods that they inherit 
    
    In summary the an ABC demands that any subclass overrides its abstract methods
    So Vehicle demands that Car & Motorcycle override the abstract method go()

 """


class Car(Vehicle):
    # Overrides Vehicle.go()
    def go(self):
        print("You drive the car")

    # Overrides Vehicle.stop()
    def stop(self):
        print("This car has stopped")


class Motorcycle(Vehicle):
    # Overrides Vehicle.go()
    def go(self):
        print("You ride the motorcycle")

    # Overrides Vehicle.stop()
    def stop(self):
        print("This motorcycle has stopped")


# vehicle = Vehicle()
# vehicle.go()
# Results in:
# TypeError: Can't instantiate abstract class Vehicle with abstract method go

# NOTE: if Vehicle has no abstract methods -> it is not an abstract class
# therefore it can be instantiated (i.e. vehicle = Vehicle() will work)

car = Car()
motorcycle = Motorcycle()

car.go()
car.stop()

motorcycle.go()
motorcycle.stop()
