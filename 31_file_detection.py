# 31 (02:43:40) file detection 📁
import os

# Check if a path exists on our computer
print("\n----- #31 File Detection -----")

# Test paths
# # -- path to some folder (exists)
path = "C:\\Users\\Billy\\Desktop"
# # -- path to some file that exists
# path = "C:\\Users\\Billy\\Desktop\\py-test.txt"
# # -- path to some file that does NOT exist
# path = "C:\\Users\\Billy\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists :)")

    # Check if a file exists on our computer
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a folder!")
else:
    print("That location doesn't exist :(")
