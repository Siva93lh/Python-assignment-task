
# Function to get the difference between the largest and smallest values

def difference_largest_smallest(arr):
    if not arr:
        return None
    largest = max(arr)
    smallest = min(arr)
    return largest - smallest

# Example array
array = [10, 230, 300, 47, 50]

difference = difference_largest_smallest(array)


if difference is not None:
    print(f"The difference between the largest and smallest values is: {difference}")
else:
    print("The array is empty, so no difference can be calculated.")