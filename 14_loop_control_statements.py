# 14 (01:17:08) Loop control statements - break | continue | pass ⛔
print("\n----- #14 Loop control statements - break | continue | pass -----")

# break     =   used to terminate the loop entirely
# continue  =   skips to the next iteration of the loop
# pass      =   does nothing, acts as a placeholder

# break = used to terminate the loop entirely
while True:
    name = input("Enter your name: ")
    if name != "" and len(name.strip()):
        break

print("Hello " + name)

# continue = skips to the next iteration of the loop
# print phone_number without the hyphens
phone_number = "123-456-7890"

for char in phone_number:
    if char == "-":
        continue
    print(char, end="")


# pass = does nothing, acts as a placeholder
# NOTE: it's like an empty if-statement block in other C-like languages
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
