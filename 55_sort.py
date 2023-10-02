# 55 (04:45:44​) sort 🗄️

# .sort() method    = used with lists
# sorted() function = used with iterables (lists, tuples, dictionaries, and sets )

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

# students_tuple.sort() # AttributeError: 'tuple' object has no attribute 'sort'

# sorted(iterable, [key=|reverse=])
# Works with lists a
# NOTE: sorted returns a list

# sorted_students = sorted(students_list)
# print(sorted_students)
# ['Mr. Krabs', 'Patrick', 'Sandy', 'Spongebob', 'Squidward']

sorted_students = sorted(students_tuple)
print(sorted_students)
print(type(sorted_students))  # <class 'list'>
# ['Mr. Krabs', 'Patrick', 'Sandy', 'Spongebob', 'Squidward']
