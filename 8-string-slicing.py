# 8 (00:40:58​) string slicing ✂️
print("\n----- #8 String Slicing -----")

# slicing = create a substring by extracting elements from another string
#       indexing[] or slice()
#       [start:stop:step]

print("### indexing[] - [start:stop:step]")

name = "Bilaal Ahmad"

### Single letter - pass index
print("\n# Extract single letter by passing index")
print("name = " + name)
print("\nname[0] = " + name[0])  # B
print("name[3] = " + name[3])  # a

### Extract first_name from name
# - [start:stop]
# NOTE: stop is exclusive

# - Bilaal Ahmad
#   ^^^^^^x         x = stop

print("\n# Extract first_name from name")
first_name = name[0:6:1]  # a
print("name[0:6:1]  = " + first_name)

# NOTE: SHORTHAND for [0:x:1]
print("-- SHORTHAND for [0:x:1]")
print("name[0:6]    = " + name[0:6])
print("name[:6]     = " + name[:6])

print("\n# Extract last_name from name")
last_name = name[7:12]
print("name[7:12]           = " + last_name)
print("name[7 : len(name)]  = " + name[7 : len(name)])

# NOTE: SHORTHAND for [0:len(str):1]
print("-- SHORTHAND for [0:last:1] | [0:len(str):1]")
print("name[7:] = " + name[7:])


### Using step to skip chars
# - [start:stop:step] - where step is the value to increment the index by when iterating from start to stop

# Extract every char at an odd index position
# - Bilaal Ahmad
#    ^ ^ ^ ^ ^ ^  x     x = stop
#    1 3 5 7 9 11 12    -->  ialAmd

print("\n# Extract every char at an odd index position")

# NOTE: use len(name) to reach char 'd' at last index position
chars_at_odd_index = name[1 : len(name) : 2]
print("name[1 : len(name) : 2]  = " + chars_at_odd_index)  # ialAmd

# SHORTHAND: use [1::2] -> to go from start to end of string by increments of 2
print("-- SHORTHAND for [1:last:2] | [1:len(name):2]")
print("name[1::2]               = " + name[1::2])  # ialAmd

# Extract every char at an even index position
# - Bilaal Ahmad
#   ^ ^ ^ ^ ^ ^  x     x = stop
#   0 2 4 6 8 10 11    -->  ialAmd

print("\n# Extract every char at an even index position")
chars_at_even_index = name[0:12:2]
print("name[0:12:2] = " + chars_at_even_index)  # Bla ha
print("name[0::2]   = " + name[0::2])  # Bla ha

# NOTE: SHORTHAND for start to end with step = [::step]
print("-- SHORTHAND for [0:12:2] | [0::2]")
print("name[::2]    = " + name[::2])  # Bla ha

print("\n# Reverse string")
# step from end of string to beginning
reversed_name = name[0:12:-1]
print("name[::-1]       = " + name[::-1])
print("Equivalent to:")
print("name[12::-1]     = " + name[12::-1])

print("\nDO NOT WORK AS EXPECTED:")
print("name[0:12:-1]    = " + reversed_name)
print("name[0::-1]      = " + name[0::-1])

# ----- Indexing[] Summary -----
# [start:stop:step]

# Start to end
# [0:end]
# [0:]

# Start to end with step
# [0:end:1]
# [0:end:2]
# [0::2]
# [::2]

# Index to end
# [index:end]
# [index:]
# e.g. [4:]

# Index to end with step
# [index:end:2]
# [index::2]

# Reverse string
# [end::-1]
# [::-1]

print("\n### Creating reusable Slice Objects")
print("slice(stop) | slice(start, stop[, step])")

# Get "http://", "google", ".com"
website = "http://google.com"
print("\n #Example 1 - " + website)

# Extract the domain "google" from "http://google.com"
# -- start slice after "http://" (scheme/protocol)
# -- end slice before ".com" (top-level domain) --> use -ve index to slice from end of string

# This slice will get the domain for any URL that starts with "http://" and ends with ".com"
slice_domain = slice(7, -4)
print("\nslice_domain: " + str(slice_domain))  # returns slice(7, -4, None)
print("website[slice_domain] = " + website[slice_domain])
# "google" from "http://google.com"

# Get URL Scheme
slice_scheme = slice(0, 7)
print("\nslice_scheme: " + str(slice_scheme))  # returns slice(0, 7, None)
print("website[slice_scheme] = " + website[slice_scheme])
# "http://" from "http://google.com"

# Get URL Top Level Domain of ".com"
slice_dot_com = slice(-4, None)
print("\nslice_top_level_domain = " + str(slice_dot_com))
print("website[slice_top_level_domain] = " + website[slice_dot_com])
# ".com" from "http://google.com"

# Verify reusability with new website
website2 = "http://wikipedia.com"
print("\n# Example 2 - " + website2)

scheme = website2[slice_scheme]
domain = website2[slice_domain]
dot_com = website2[slice_dot_com]

print("scheme = " + scheme)
print("domain = " + domain)
print("dot_com = " + dot_com)
