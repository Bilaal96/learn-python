# 19 (01:40:03​) dictionaries 📖
# Mutable, unordered collection of unique key-value pairs
# Fast because they use hashing - AKA Hash Tables
# Allows us to access a value quickly
print("\n----- #19 Dictionaries -----")

capitals = {
    "USA": "Washington D.C.",
    "England": "Birmingham",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
}

# Access via key
print(capitals["Russia"])  # Moscow
print()

# Accessing key that doesn't exist using indexing will result in a KeyError
# print(capitals["Germany"])  # KeyError: 'Germany'

# Access non-existent key safely (i.e. without causing error)
print(capitals.get("Germany"))  # None
print()

# NOTE: these methods return a "set-like" object
# Print all keys
print(capitals.keys())
# dict_keys(['USA', 'England', 'India', 'China', 'Russia'])
print()


# Print all values
print(capitals.values())
# dict_values(['Washington D.C.', 'London', 'New Delhi', 'Beijing', 'Moscow'])
print()


# Print all key-value pairs
print(capitals.items())
# dict_items([('USA', 'Washington D.C.'), ('England', 'London'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow')])
print()


# Modify / update a dictionary
# Add Germany: Berlin
capitals.update({"Germany": "Berlin"})
# Update value of existing key
capitals.update({"England": "London"})

# Remove the key-value pair corresponding to the provided key
capitals.pop("China")

# Iterate keys & values of a dictionary using D.items()
# for key, value in D.items():
for country, capital in capitals.items():
    print(f"{country}: {capital}")
print("capitals size:", str(capitals.__len__()))
print()


# Remove all key-value pairs
capitals.clear()
print("capitals.clear()")
print("capitals size:", str(capitals.__len__()))
