
# Program to check whether a number is EVEN or ODD using a switch-like structure

def check_even_odd(num):
    # Dictionary mimicking a switch-case structure
    switch = {
        0: "Even",
        1: "Odd"
    }
    
    return switch.get(num % 2, "Invalid input")


number = int(input("Enter a number: "))

# Check and print the result
result = check_even_odd(number)
print(f"The number {number} is {result}.")