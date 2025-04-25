
# Function to find the second largest number in an array

def find_second_largest(arr):
    if len(arr) < 2:
        return None
    unique_numbers = list(set(arr))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) >   1 else None

array = [10, 20, 30, 40, 50, 20, 30]

second_largest = find_second_largest(array)


if second_largest is not None:
    print(f"The second largest number in the array is: {second_largest}")
else:
    print("The array does not have enough unique elements to find the second largest number.")