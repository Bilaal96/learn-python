# 25 (02:09:40​) variable scope 🔬
# Refers to region / block of code in which a variable is accessible
print("\n----- #25 Variable Scope -----")

# Global Scope - available in global and local scope
name = "Bilaal"


def get_name():
    # local scope
    # Variables defined within the local scope with the same name as variables...
    # in the outer scope will take precedence
    name = "Billy"  # variable accessible within the local scope
    return name


def get_global_name():
    return name


print("Local scope (get_name):", get_name())
print("Global scope (name var):", name)
print("Global scope (get_global_name):", get_global_name())

# LEGB Rule - Python looks for var assignment in the order of the following scope/environments
# L = Local
# E = Enclosing
# G = Global
# B = Built-in
