# 35 (02:57:05​) move a file 🗃️
import os
import shutil  # shutil.move() is used to move file between disk drives

print("\n----- #35 Move A File -----")

# location of where source file is located
source = "35-move-file-bro-code.txt"
# destination to move source file to
destination = f"C:\\Users\\Billy\\Desktop\\{source}"
# destination = f"C:\\Users\\Billy\\Desktop\\35-test.txt"


# Move a file from current dir to desktop
def move_file_to_desktop(source, destination):
    try:
        # Prevent overwriting of existing file at destination via file detection
        if os.path.exists(destination):
            print(f"That file already exists at: {destination}")
            print(f"I have not been programmed to overwrite existing files")
        else:
            if os.path.exists(source):
                print(f"Found {source} in the current directory")
            else:
                # Create the source file in current dir if it doesn't exist
                with open(source, "w") as file:
                    file.write(
                        "This file is to be moved to the Desktop from Bro Code directory"
                    )
                    print(f"{source} was created successfully")

            # Used to rename/move a file on the same hard disk
            # NOTE: os.replace() cannot move files between hard disks
            # It throws an OSError if an attempt to do so is made
            os.replace(source, destination)
            print(source + " was moved successfully")
    except FileNotFoundError as e:
        print(f"File {e.filename} was not found")
    except OSError as e:
        # Handle moving files between disk drives
        if e.strerror == "The system cannot move the file to a different disk drive":
            shutil.move(source, destination)
            print(source + " was moved successfully")
        else:
            print(e)
    except Exception as e:
        print(e)


# move_file_to_desktop(source, destination)


# Paths options:
# https://stackoverflow.com/questions/19065115/python-windows-path-slash
# https://stackoverflow.com/questions/63582650/replace-slashes-in-os-getcwd


# write to file
# create & write to file if it doesn't exist
def write_file(name, content=""):
    with open(name, "w") as file:
        file.write(content)


# Create a dir locally (in current dir) and move file to it# args: source, local_dir
# Check if local_dir exists
# -- doesn't exist --> create it
# Check if local file exists
# 1 - get path to local file
# 2 - check if it exist
# -- exists --> move to local dir
# -- doesn't exist --> create it using write_file() (above)
def move_file_to_local_dir(local_file, local_dir):
    try:
        print("\n### Create a dir locally (in current dir) and move file to it")

        # Get absolute path to local_dir
        cwd = os.getcwd()
        local_dir_path = os.path.join(cwd, local_dir)
        print("local_dir exists?", str(os.path.exists(local_dir_path)))

        # Create local_dir if it doesn't already exist
        if not os.path.exists(local_dir_path):
            os.mkdir(local_dir_path)
            print("local_dir created")

        print("local_dir (abs path):", local_dir_path)

        # Create local_file if it doesn't already exist
        if not os.path.exists(local_file):
            write_file(local_file, "This file migrated from the root directory")

        # Move local_file into local_dir
        os.replace(
            local_file,
            os.path.join(local_dir_path, "35-file-migrated-from-parent-dir.txt"),
        )

    except Exception as e:
        print(e)


local_dir_name = "35-local-dir"
local_file_name = "35-file-to-move-locally.txt"

# move_file_to_local_dir(local_file_name, local_dir_name)
