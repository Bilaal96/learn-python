# 23 (02:04:51) keyword arguments 🔑
print("\n----- #23 Keyword Arguments -----")
# keyword arguments --> allow you to map arguments to parameters by...
# preceding the argument value with an identifier that matches the parameter name

# -- passed to a function like so: fn(arg_name=<argument>, ...)
# -- they allow you to pass arguments in any order as long as the identifier matches a parameter
# -- number of arguments must still match number of parameters


def hello(first, middle, last):
    print(f"Hello {first} {middle} {last}")


# Keyword arguments - arguments are prefixed with an identifier & passed in different order compared to parameters
hello(last="Kent", first="Clark", middle="Kal-el")
