import time
import sys

# 20 (01:47:20​) indexing 📑
# index operator [] = gives access to a sequence's element (str, list, tuples & more)
print("\n----- #20 Indexing -----")

name = "bro Code!"

if name[0].islower():
    print(f"{name[0]} is lowercase. Capitalizing...")

    # Simulate processing
    sys.stdout.write("Loading")
    for i in range(3):
        # print(".", end="")
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\n")

    print("Capitalization complete.\n")
    name = name.capitalize()
    print(name)

# String slicing via indexing
first_name = name[:3].upper()
last_name = name[4:-1].lower()

last_char = name[-1]

print(first_name)
print(last_name)
print(last_char)
