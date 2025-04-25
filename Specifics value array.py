
# Function to test if an array contains a specific value
def contains_value(arr, value):
    return value in arr 

array = [10, 20, 30, 40, 50]

value_to_find = int(input("Enter the value to check if it exists in the array: "))

if contains_value(array, value_to_find):
    print(f"The array contains the value {value_to_find}.")
else:
    print(f"The array does not contain the value {value_to_find}.")