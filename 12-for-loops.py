# 12 (01:07:31​) for loops ➰
print("\n----- #12 For Loops -----")

# for loops can be used to iterate any iterable:
# i.e. string or any collection

# range(stop)
# range(start, stop[, step]) -> step is optional
# NOTE: stop arg is always exclusive

# * To make the stop arg inclusive, add 1 to stop:
# range(start, stop + 1)

print("\n### Iterate range() with For Loop")

# 0-9 (exclusive of 10)
# for i in range(10):
#     print(i)

# 0-10 (inclusive of 10)
# for i in range(10 + 1):
#     print(i)

# 1-10
# for i in range(10):
#     print(i + 1)


# 50-60
# for i in range(50, 60 + 1):
#     print(i)

# Even numbers from 50-60
for second in range(50, 60 + 1, 2):
    print(second)

print("\n### Iterate String with For Loop")

for second in "Bilaal Ahmad":
    print(second)

# ---------------------------------------------------------------------------- #
print("\n### Countdown timer using For Loop & time module")

import time

# https://docs.python.org/3/library/time.html

# print(time.time()) # number of seconds passed from unix epoch (1 Jan 1970 00:00:00 UTC)
# https://docs.python.org/3/library/time.html#time.time
# https://www.wikiwand.com/en/Unix_time

# Countdown from 10 to 1 by: printing second, after every second that passes in real-time
for second in range(10, 0, -1):
    print(second)
    time.sleep(1)
    # https://docs.python.org/3/library/time.html#time.sleep

print("Happy new year!")
