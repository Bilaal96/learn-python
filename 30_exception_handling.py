# 30 (02:36:43​) exception handling ⚠️
print("\n----- #30 Exception Handling -----")

# An event detected during execution that interrupts the flow of a program


# Cause an exception by entering an impossible division
# - e.g. by dividing by zero --> ZeroDivisionError: division by zero
# We will gracefully handle the exception without interrupting the flow of our program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

# Use "as" to alias the exception thrown as "e"
# Now "e" can be referenced to access the error message
except ZeroDivisionError as e:
    print("Error caused by:", e)
    print("You can't divide by 0! Idiot!")

except ValueError as e:
    print("Error caused by:", e)
    print("You can only enter numbers!")

# "except Exception" catches all types of exceptions thrown
# any unhandled error will be handled by "except Exception"
except Exception as e:
    print("Error caused by:", e)
    print("Something went wrong :(")

# If there are no exceptions, do something else
# NOTE: This will NEVER run if there IS an exception
else:
    # NOTE: observe how result from the try-block is accessible in the else-block
    print(result)

# NOTE: This will ALWAYS run, even if there IS an exception
# Often times if we open files, we should/can use the finally-block to close them
finally:
    print("finally: will always execute.")
    print("Exit program...")

# NOTE: It is best practice to handle each specific type of exception that you expect to be thrown
# Only then should you use "except Exception" to catch errors that you may not have thought to handle
