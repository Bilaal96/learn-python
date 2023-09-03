# 21 (01:53:23​) functions 📞
print("\n----- #21 Functions -----")


def hello(first_name=None, last_name=None):
    greeting = "Hello"
    if first_name:
        greeting += f" {first_name}"
    if last_name:
        greeting += f" {last_name}!"
    else:
        greeting += "!"
    print(greeting)


hello()
hello("Bruce")
hello("Clark")
hello("Barry", "Allen")
