# 55 (04:45:44​) sort 🗄️

# .sort() method    = used with lists
# -- sort in-place (i.e. mutates the list)

# sorted() function = used with iterables (lists, tuples, dictionaries, and sets)
# -- returns a new sorted list

students_list = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

# NOTE: the method mutates the original list

print("--- List.sort() method ---")
# Sort list alphabetically
# students.sort()
""" 
    List order:
    Mr. Krabs -> first
    Patrick  
    Sandy    
    Spongebob
    Squidward -> last
 """

# Sort accepts 2 optional kwargs (key-word arguments): reverse= or key=
# reverse=True -> sort list alphabetically in reverse order
students_list.sort(reverse=True)
""" 
    Squidward -> first
    Spongebob
    Sandy
    Patrick
    Mr. Krabs -> last
 """

for s in students_list:
    print(s)

print("\n--- sorted() function for iterables ---")

students_tuple = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")

# .sort() method only accepts lists as an argument

# e.g. tuple.sort() will throw error
# students_tuple.sort()
""" 
    AttributeError: 'tuple' object has no attribute 'sort'
 """

# sorted(iterable, [key=|reverse=]) -> works with all iterables
# Where iterable is one of lists, tuples, dictionaries, and sets
# NOTE: sorted() fn returns a list

# e.g. using sorted() fn to sort a list
# sorted_students = sorted(students_list)
""" 
    Mr. Krabs
    Patrick
    Sandy
    Spongebob
    Squidward
 """

# sorted_students = sorted(students_tuple)
# print(type(sorted_students))  # <class 'list'> --> returns list
""" 
    Mr. Krabs
    Patrick
    Sandy
    Spongebob
    Squidward
 """

sorted_students = sorted(students_tuple, reverse=True)
# print(type(sorted_students))  # <class 'list'> --> returns list
""" 
    Squidward
    Spongebob
    Sandy
    Patrick
    Mr. Krabs
 """

for s in sorted_students:
    print(s)

print("\n--- Sorting Complex Lists ---")

# List of tuples : (name, grade, age)
student_record = [
    ("Bob", "F", 14),
    ("Sally", "A", 21),
    ("May", "D", 60),
    ("John", "B", 27),
    ("Charlie", "C", 17),
]

# Sorts the list of tuples alphabetically by the first key
# student_record.sort()
""" 
    ('Bob', 'F', 14)
    ('Charlie', 'C', 17)
    ('John', 'B', 27)
    ('May', 'D', 60)
    ('Sally', 'A', 21)
 """

# Sort by another key of the iterable using key=
# key= accepts a function object (as a value) that returns the index of the iterable to sort by
by_grade = lambda record: record[1]  # Sort by index 1 (i.e. grade)
# student_record.sort(key=by_grade)
# student_record.sort(key=lambda record: record[1]) # in one line
""" 
    ('Sally', 'A', 21) --> highest grade first
    ('John', 'B', 27)
    ('Charlie', 'C', 17)
    ('May', 'D', 60)
    ('Bob', 'F', 14)
 """

# Sort by grade, in reverse order
student_record.sort(key=by_grade, reverse=True)
""" 
    ('Bob', 'F', 14)
    ('May', 'D', 60)
    ('Charlie', 'C', 17)
    ('John', 'B', 27)
    ('Sally', 'A', 21)
 """

# Sort by age
by_age = lambda record: record[2]

# Sort by age, ascending
# student_record.sort(key=by_age)
""" 
    ('Bob', 'F', 14)
    ('Charlie', 'C', 17)
    ('Sally', 'A', 21)
    ('John', 'B', 27)
    ('May', 'D', 60)
 """

# Sort by age, descending
student_record.sort(key=by_age, reverse=True)
""" 
    ('May', 'D', 60)
    ('John', 'B', 27)
    ('Sally', 'A', 21)
    ('Charlie', 'C', 17)
    ('Bob', 'F', 14)
 """

for r in student_record:
    print(r)


print("\n--- Sorting Complex Tuples ---")
# Tuple of tuples : (name, grade, score)
student_record_tuple = (
    ("Bob", "F", 50),
    ("Sally", "A", 21),
    ("May", "D", 60),
    ("John", "B", 80),
    ("Steve", "C", 70),
)

# NOTE: remember that only List's have a .sort() method
# As we're using a tuple in this example, we must use the sorted() fn

# Sort by name - i.e. the zero index in each record (where record=item in the tuple)
# defaults to key=lambda record: record[0]
# sorted_student_record = sorted(student_record_tuple)
""" 
    ('Bob', 'F', 50)
    ('John', 'B', 80)
    ('May', 'D', 60)
    ('Sally', 'A', 21)
    ('Steve', 'C', 70)
 """

# Sort by grade
by_grade = lambda record: record[1]
sorted_student_record = sorted(student_record_tuple, key=by_grade)
""" 
    ('Sally', 'A', 21)
    ('John', 'B', 80)
    ('Steve', 'C', 70)
    ('May', 'D', 60)
    ('Bob', 'F', 50) 
 """

# Sort by age, in reverse order
by_age = lambda record: record[2]
sorted_student_record = sorted(student_record_tuple, key=by_age, reverse=True)
""" 
    ('John', 'B', 80)
    ('Steve', 'C', 70)
    ('May', 'D', 60)
    ('Bob', 'F', 50)
    ('Sally', 'A', 21)
 """

for r in sorted_student_record:
    print(r)
