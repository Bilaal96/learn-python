import signal


# Detect CTRL+C and exit terminal
def signal_handler(sig, frame):
    print("\n")
    print("Exited with code: " + str(signal.SIGINT))
    exit(sig)


signal.signal(signal.SIGINT, signal_handler)

# 10 (00:58:19)​ logical operators 🔣
print("\n----- #10 Logical Operators -----")

# NOTE: python uses the literal words rather than symbolic syntax: && || !
# and | or | not

while True:
    temp = float(input("What is the temperature outside (in celsius)?: "))

    if temp > 35 or temp < 18:
        print("The weather is bad :(")

    # negate multiple conditions by wrapping them in parentheses
    if not (temp > 35 or temp < 18):
        print("The weather is good :)")

    if temp > 35:
        print("It's scorching hot!")
    elif temp > 28:
        print("It's boiling today!")
    elif temp >= 24:
        print("It's hot today")
    elif temp >= 18:
        print("It's warm today")
    elif temp <= 17 and temp >= 13:
        print("It's chilly today")
    elif temp < 13 and temp >= 7:
        print("It's cold today!")
    else:
        print("It's freezing today!")
