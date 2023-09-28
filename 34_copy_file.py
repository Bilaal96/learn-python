# 34 (02:53:45​) copy a file 🖨️
print("\n----- #34 Copy A File -----")

# copyfile() = copies contents of a file
# copy()     = copyfile + permission mode + destination can be a directory
# copy2()    = copy + copies metadata (file's creation & modification times)

# There are other ways to do this too, but we'll do so using the shutil module
# NOTE: this module gives us access to the methods outlined above

# We'll be using shutil.copyfile() to the copy previously created .txt files
import shutil

# args: src, destination
# Copy "33-write-file.txt" from current dir to "34-copy-file.txt" file in the same dir
# NOTE: a full path can be given to copy elsewhere on your computer
shutil.copyfile("33-write-file.txt", "34-copy-file.txt")

# NOTE: arguments are the same for copy() & copy2()
