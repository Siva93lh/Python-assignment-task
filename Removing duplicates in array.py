
# Function to remove duplicate elements from an array
def remove_duplicates(arr):
    return list(set(arr))  # Convert to set to remove duplicates, then back to list

# Example array with duplicates
array = [10, 20, 30, 20, 40, 50, 10, 30]

# Call the function to remove duplicates
unique_array = remove_duplicates(array)

# Print the new array with unique elements
print("Original array:", array)
print("Array with duplicates removed:", unique_array)

