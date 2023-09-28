# 36 (03:01:20​) delete a file 🗑️
import os
import time
import shutil

print("\n----- #36 Delete A File -----")


# write to file
# create & write to file if it doesn't exist
def write_file(name, content=""):
    with open(name, "w") as file:
        file.write(content)
        print(f"{name} created successfully")


def rm_file(file_path):
    try:
        # If file is local to current .py file, simply pass the filename as is
        # Otherwise provide an absolute path to the file
        # os.remove() - raises FileNotFoundError if the path is receives doesn't exist
        os.remove(file_path)
        print(f"{file_path} removed successfully")

    except FileNotFoundError as e:
        print(f"{e.filename} was not found")
    except OSError as e:
        print(
            "The path provided must point to a file not a directory. To remove a directory use os.rmdir()"
        )
    except Exception as e:
        print(e)


def rm_dir(dir_path):
    try:
        # os.rmdir - file must be empty to remove it, otherwise an error occurs
        os.rmdir(dir_path)
        print(f"/{dir_path} removed successfully")
    except OSError as e:
        print(f"Attempt to remove /{dir_path} failed")
        print(e.strerror)

        print("Now attempting to remove recursively")
        if os.path.exists(dir_path):
            shutil.rmtree(dir_path)
            print(f"shutil.rmtree() successfully removed {dir_path}")
        else:
            print(
                f"shutil.rmtree() failed to remove {dir_path} recursively because it doesn't exist"
            )

    except Exception as e:
        print(type(e))
        print(e)
    # except Exception as e:
    # print(e)
    finally:
        print()


file_to_delete = "36-lame-file-to-delete.txt"
write_file(file_to_delete, "PLEASE DELETE ME, I SO LAME")


print("\n# Remove file")
rm_file(file_to_delete)


print("\n# Attempt to remove dir")
local_dir_name = "35-local-dir"
local_dir_abs_path = os.path.join(os.getcwd(), local_dir_name)
rm_file(local_dir_abs_path)
rm_file(local_dir_name)  # OSError: attempt to remove dir, not file

print("\n# Remove directory")
rm_dir(local_dir_name)  # The directory is not empty: '35-local-dir'

dir_to_remove = "36-dir-to-remove"
if not os.path.exists(dir_to_remove):
    os.mkdir(dir_to_remove)
    time.sleep(1)

rm_dir(dir_to_remove)
