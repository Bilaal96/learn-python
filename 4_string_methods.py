# 4   (00:20:27​) string methods 〰️
print("\n----- #4 String Methods -----")
me = "Bilaal Ahmad"

print("# len() - return length of str")
print(len(me))  # 3 (int)

print("\n# .find() - get index of first occurrence of the given char in str")
print(me.find("B"))  # 0
print(me.find("i"))  # 1
print(me.find("a"))  # 3
print(me.find("A"))  # 7

print("\n# .capitalize() - convert first char to uppercase and rest to lowercase")
print(me.capitalize())
print("# .upper() - convert to uppercase")
print(me.upper())
print("# .lower() - convert to lowercase")
print(me.lower())

print("\n# .isdigit() - return True if digit, False if not")
print(me.isdigit())  # False - all str chars
# A string is a digit string if all characters in the string are digits and there is at least one character in the string.

print("123".isdigit())  # True - all digits
print("123.4".isdigit())  # False - includes decimal char, not all digits

print("\n# .isalpha() - return True if alphabetic, False if not")
print(me.isalpha())  # False - includes whitespace
print("27Aug23".isalpha())  # False - includes numbers
print("Bilaal-Ahmad".isalpha())  # False - includes hyphen
print("Hello".isalpha())  # True - all alphabetic

print("\n# .count() - return int of occurrences of a substring within a string")
print(me.count("a"))  # 3 lowercase "a"
print(me.count("l"))  # 2 lowercase "l"
print(me.count("A"))  # 1 uppercase "A"
print(me.count("z"))  # 0 lowercase "z"

print(
    "\n# .replace(old, new) - replace old substring with new substring & return resulting str"
)
print(me.replace("aal", "ly"))  # Billy Ahmad

#
print("\n# print('str' * int) - Shorthand to print string multiple times")

print("Bro " * 3)  # BroBroBro
