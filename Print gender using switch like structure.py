
# Program to print gender (Male/Female) based on input M/F using switch-like structure

def print_gender(gender):
    # Dictionary mimicking a switch-case structure
    switch = {
        'M': "Male",
        'F': "Female"
    }
    
    return switch.get(gender.upper(), "Invalid input")


gender_input = input("Enter gender (M/F): ")

gender = print_gender(gender_input)
print(f"The gender is: {gender}")
