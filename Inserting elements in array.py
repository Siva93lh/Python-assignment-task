
# Function to insert an element at a specific position in the array
def insert_element(arr, element, position):
    arr.insert(position, element)

array = [10, 20, 30, 40, 50]

element_to_insert = int(input("Enter the element to insert: "))
position_to_insert = int(input("Enter the position to insert the element at: "))

insert_element(array, element_to_insert, position_to_insert)

print("Updated array:", array)