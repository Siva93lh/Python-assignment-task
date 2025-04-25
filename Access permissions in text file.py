
#. Program to check read and write access permissions
import os

def check_permissions(file_path):
    # Check if the file has read permission
    can_read = os.access(file_path, os.R_OK)

    # Check if the file has write permission
    can_write = os.access(file_path, os.W_OK)

    # Print results
    if can_read:
        print(f"The file '{file_path}' has read access.")
    else:
        print(f"The file '{file_path}' does not have read access.")

    if can_write:
        print(f"The file '{file_path}' has write access.")
    else:
     print(f"The file '{file_path}' does not have write access.")

# Test the function with a sample file path
file_path = 'sample.txt'  # Replace with your file path
check_permissions(file_path)

# Check if the file has execute permission
can_execute = os.access(file_path, os.X_OK)
if can_execute:
    print(f"The file '{file_path}' has execute access.")
else:
    print(f"The file '{file_path}' does not have execute access.")