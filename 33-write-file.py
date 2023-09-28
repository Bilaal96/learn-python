# 33 (02:51:00​) write a file 📝
print("\n----- #33 Write File -----")

# Write to the file of the given name
# If it does not exist, create it and then write to it

# NOTE: The open function has a 2nd "mode" parameter
# By default it is "r" for read
# ... or verbosely: open('file.txt', 'r')

# To write to a file, we must set the mode to 'w' for write
# i.e. open it in write mode
# NOTE: in write mode, the string passed to file.write() will overwrite the existing file contents
text = "Yoooooooo\nThis is some text\nHave a good one\n"
# text = "Uh oh! This text has been overwritten\n"
text = "This text has been appended\n"

# To append text to a file with existing content, set the mode to 'a' for append

with open("33-write-file.txt", "a") as file:
    file.write(text)
