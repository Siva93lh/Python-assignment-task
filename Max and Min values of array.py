
# Function to find the minimum and maximum values of an array
def find_min_max(arr):
    if not arr: 
        return None, None  
    return min(arr), max(arr) 

# Example array
array = [10, 25, 35, 46, 52, 99, 101]

min_value, max_value = find_min_max(array)

# Print the results
print(f"The minimum value in the array is: {min_value}")
print(f"The maximum value in the array is: {max_value}")