# 9 (00:51:52​) if statements 🤔
print("\n----- #0 if-statements -----")
age = int(input("How old are you?: "))
print("")

if age == 100:
    print("Congrats on making it to 100 years old")
if age >= 18:
    print("You are an adult")
elif age == 17:
    print(
        "You're technically a child, but it is legal for you to start driving lessons"
    )
elif age < 0:
    print("You have not been born yet")
    exit()
else:
    print("You are a child")

print("")


# UK - must be at least 17
def can_take_driving_lessons(age):
    return age >= 17


# UK - must be at least 18
def can_drink_alcohol(age):
    return age >= 18


# old enough to both drink and drive
if can_drink_alcohol(age):
    print("Never drink and drive!")
# can't drink but can drive
elif not can_drink_alcohol(age) and can_take_driving_lessons(age):
    print("Focus on getting your license.")
    print("Underage drinking is illegal!")
else:
    print("Sorry you'll have to wait until you're of legal age to drive or drink.")
    print("But remember, never do both at the same time!")

print("")
