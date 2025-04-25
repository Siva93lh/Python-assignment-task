
# Function to find duplicate values in an array
def find_duplicates(arr):
    seen = set()
    duplicates = set()  
    for value in arr:
        if value in seen:
            duplicates.add(value)  
        else:
            seen.add(value) 
    return list(duplicates)  

array = [10, 20, 30, 40, 50, 20, 30, 60]

duplicates = find_duplicates(array)

if duplicates:
    print(f"Duplicate values in the array are: {duplicates}")
else:
    print("No duplicate values found in the array.")