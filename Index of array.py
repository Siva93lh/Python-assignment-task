
# Function to find the index of an element in an array
def find_index(arr, element):
    if element in arr:
        return arr.index(element)  # Return the index of the element
    else:
        return -1  # Return -1 if the element is not found

# Example array
array = [10, 20, 30, 40, 50]

# Input the element to search for
element_to_find = int(input("Enter the element to find the index: "))

# Call the function and print the result
index = find_index(array, element_to_find)

if index != -1:
    print(f"The index of {element_to_find} is: {index}")
else:
    print(f"{element_to_find} not found in the array.")