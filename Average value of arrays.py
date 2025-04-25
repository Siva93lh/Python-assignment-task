
# Function to calculate the average value of an array
def average_of_array(arr):
    if len(arr) == 0:
        return 0  # Avoid division by zero if the array is empty
    return sum(arr) / len(arr)

# Example array of integers
array = [10, 20, 30, 40, 50]

# Call the function and print the result
result = average_of_array(array)
print(f"The average of the array is: {result}")