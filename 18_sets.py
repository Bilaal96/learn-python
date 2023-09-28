# 18 (01:33:47​) sets 🍴
# A set is a collection that is unordered, un-indexed & CANNOT contain duplicate values
print("\n----- #18 Sets -----")


def print_set(set: set, print_new_line=True):
    if set.__len__() == 0:
        print("Empty set...")
        return
    for item in set:
        print(item)
    if print_new_line:
        print()


print("\n### Set Basics")

# NOTE a set is denoted with curly braces
utensils = {"fork", "spoon", "knife"}

# NOTE: the set is UNORDERED --> printing them does not guarantee
# that they will be in the same in order in which they were defined (above)
print("Set: utensils")
print_set(utensils)

# E.g. when attempting to run this file multiple times I got the following output
# __ Run 1 __       __ Run 2 __         __ Run 3 __
# fork              spoon               fork
# spoon             knife               knife
# knife             fork                spoon

# NOTE: A set is faster than a list if you need to check that something exists within a set


# Sets store unique values. Observe below how,
# when you enter the same value multiple times,
# the interpreter only parses "knife" once
cutlery = {"fork", "spoon", "knife", "knife", "knife"}

print("Set: cutlery")
print_set(cutlery)  # only prints knife once


print("\n### Set Methods")

# Add element to set
cutlery.add("napkin")
cutlery.remove("fork")
cutlery.clear()

print("Set: cutlery")
print_set(cutlery, False)

# Working with multiple sets
dishes = {"bowl", "plate", "cup", "knife"}  # NOTE: share knife in common with utensils

# Update a set with the union of itself and others.
print("\n# .update() - uncomment to test")
# utensils.update(dishes)  # adds elements of dishes to utensils
# print("Set: utensils")
# print_set(utensils)

# NOTE: .update() mutates the argument - i.e. moves all elements from dishes to utensils

# Return the union of sets as a NEW set (i.e. all elements that are in either set)
print("\n# .union() - uncomment to test")
# dinner_table = utensils.union(dishes)
# # dinner_table = dishes.union(utensils) # This would accomplish the same
# print("Set: dinner_table")
# print_set(dinner_table)

# Return all elements that are in the applied set but not the others
# -- applied set meaning the set that the method is applied to
print("\n# .difference() - uncomment to test")
# print("Set: elements unique to 'utensils' when compared with 'dishes'")
# print(utensils.difference(dishes))

# print("Set: elements unique to 'dishes' when compared with 'utensils'")
# print(dishes.difference(utensils))

print("\n# .intersection() - uncomment to test")
print("Set: elements shared in common between 'utensils' and 'dishes's")
print(utensils.intersection(dishes))
