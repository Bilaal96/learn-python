# 32 (02:47:28​) read a file 🔍
print("\n----- #32 Read File -----")

# Absolute or relative file path
# Or just the filename if file is stored locally

# Open and read the file at the given path
# If complete path is not provided, python will look in the current directory
# ! NOTE: in some cases, you have to manually close a file once it has been opened and you're finished with it
# * NOTE: when using a with-statement to open & read a file, the file is automatically closed

# NOTE: The open function has a 2nd "mode" parameter
# By default it is read or verbosely: open('file.txt', 'r')
try:
    with open("32-read-file.txt") as file:
        print(file.read())

    # Check whether the file is closed or not
    # file.closed returns a boolean
    print("\nIs file closed?: " + str(file.closed))  # True
except FileNotFoundError as e:
    print(f"File '{e.filename}' was not found")
