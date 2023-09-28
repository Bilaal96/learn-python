# Small script I wrote to convert all filenames from kebab-case to snake_case
from os import listdir, rename
from os.path import isfile

def kebab_to_snake_case(filename):
    # Skip files that don't contain hyphens
    if "-" in filename:
        new_filename = filename.replace("-", "_")
        rename(filename, new_filename)

for filename in listdir():
    # ignore directories
    if not isfile(filename): continue

    kebab_to_snake_case(filename)

print(listdir())