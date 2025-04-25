 
#Function to remove a specific element from an array
def remove_element(arr, value):
    if value in arr:
        arr.remove(value)
        return True
    else:
        return False

array = [10, 20, 30, 40, 50]

value_to_remove = int(input("Enter the value to remove from the array: "))

if remove_element(array, value_to_remove):
    print(f"The value {value_to_remove} has been removed.")
    print("Updated array:", array)
else:
    print(f"The value {value_to_remove} was not found in the array.")
