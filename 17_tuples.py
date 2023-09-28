# 17 (01:30:47​) tuples 📄
# Tuples are a type of collection that is similar to lists EXCEPT they're ORDERED and UNCHANGEABLE (IMMUTABLE)
# They're used to group together related data

print("\n----- #17 Tuples -----")

student = ("Bilaal", 27, "male")  # name | age | gender

# Tuple Methods
# Tuple.count() = Return number of occurrences of a given value
print(student.count("Bilaal"))  # 1

# Tuple.index() = Return index of a given value
print(student.index("male"))  # 2

# Iterate over items of tuple
for item in student:
    print(item)

# Check for value in Tuple
if "Bilaal" in student:
    print("Student's name is " + student[0])
