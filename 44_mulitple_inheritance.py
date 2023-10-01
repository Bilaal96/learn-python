# 44 (03:58:32) multiple inheritance 👨‍👩‍👧‍👦

# When a child class is derived from more than one parent class

# NOTE: in nature, an animal can be both prey and predator
# e.g. larger fish often consume smaller fish
# i.e. a fish may hunt smaller fish, and be hunted by larger fish


class Prey:
    def flee(self):
        print("This animal flees")


class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass


class Hawk(Predator):
    pass


# Multiple inheritance - inherits from 2 (or more) parent classes
class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# Prey
rabbit.flee()

# Predator
hawk.hunt()

# Prey & Predator
fish.flee()
fish.hunt()
