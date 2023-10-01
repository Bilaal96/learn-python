# 50 (04:23:20​) duck typing 🦆

""" 
    duck typing = concept where the class of an object is less 
    important that the methods/attributes that the class may have
    
    The class type is NOT checked if the minimum methods/attributes are present

    Based of popular phrase:
    "If walks like a duck, and it quacks like a duck, then it must be a duck"

    Summary:
    * minimum attributes & methods > class type
    
 """


class Duck:
    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is quacking")

    def swim(self):
        print("This duck is swimming")


class Chicken:
    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

    def sleep(self):
        print("This chicken is sleeping")


# Here is a person class, that is designed to catch ducks
class Person:
    def catch(self, duck):
        # This code works for catching chickens (demo'd below)
        # Because we have not validated that duck is an instance of Duck
        # So any object passed in that implements the methods used below
        # (walk & talk) will work
        duck.walk()
        duck.talk()

        # duck.swim() will cause an error when we pass in a chicken object
        # because it does not implement the swim() method
        # duck.swim()
        # AttributeError: 'Chicken' object has no attribute 'swim'
        print("You caught t he critter!")


duck = Duck()
chicken = Chicken()
person = Person()

# Successfully catches a duck
person.catch(duck)

# Successfully catches a chicken with method written to catch a duck
# NOTE: this still works because chicken implements the same methods as duck
# and as a result, a chicken can be substituted for a duck
person.catch(chicken)
