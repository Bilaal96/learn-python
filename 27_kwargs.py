# 27 (02:16:58​) **kwargs 🎁
print("\n----- #27 **kwargs -----")

# - *kwargs - a function parameter that allows you to pass a varying number of keyword (or key-value) arguments to a function
# - *kwargs accumulates the arguments within a dictionary


def keywordHello(first, last):
    print(f"Hello {first} {last}")


# only accepts 2 arguments
keywordHello(last="Rodgers", first="Steve")

#! TypeError: keywordHello() got an unexpected keyword argument 'middle'
# keywordHello(last="Code", middle="Dude", first="Bro")


def kwargsHello(**names):  # - **kwargs can give any name
    print("Hello", end=" ")
    for name in names.values():
        print(name, end=" ")


kwargsHello(title="Mr.", first="Peter", middle="B.", last="Parker")
