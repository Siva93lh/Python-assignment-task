
# Function to copy an array to another array
def copy_array(source_array):
    return source_array.copy()   

array1 = [10, 20, 30, 40, 50]

array2 = copy_array(array1)

print("Original array:", array1)
print("Copied array:", array2)
