# 37 (03:06:15​) modules 💌

# module = a file containing python code. May contain functions, classes, etc.
# Used with modular programming, which is to separate a program into parts

""" 
    In Python a module can be visualised as an object, containing variables and methods.

    The filename corresponds to the module name.

    Modules in python don't work the same way as JS modules.
    E.g. you cannot import a module from a local directory in your project folder.
    If you want to import from a folder, the folder must be marked as a package - then you can import from the package.
 """

# import message_module_37
# Access methods like:
# message_module_37.hello()
# message_module_37.bye()


# Apply alias to module name to shorten it
# import message_module_37 as msg
# Access methods like:
# msg.hello()
# msg.bye()


# Import individual methods
# from <module_name> import <method_0> [,<method_n>]
# from message_module_37 import hello, bye
# hello()
# bye()


# Import every method in the module by name
# NOTE: AVOID FOR LARGE PROJECTS TO AVOID NAME CONFLICTS BETWEEN MODULES
from message_module_37 import *

print("\n----- #37 Modules -----")

hello()
bye()


# View comprehensive list of built-in modules
help("modules")

# You can also view this in the docs at: Python Module Index
