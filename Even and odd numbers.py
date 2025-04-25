
# Program to print odd and even numbers from 1 to 20

# Print even numbers
print("Even numbers:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# Print odd numbers
print("\nOdd numbers:")
for num in range(1, 21):
    if num % 2 != 0:
        print(num)