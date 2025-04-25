
# Function to verify if the array contains two specified elements (12, 23)
def contains_elements(arr, elem1, elem2):
    return elem1 in arr and elem2 in arr

# Example array
array = [10, 12, 15, 23, 30]

# Call the function to check for elements 12 and 23
result = contains_elements(array, 12, 23)

if result:
    print("The array contains both 12 and 23.")
else:
    print("The array does not contain both 12 and 23.")



