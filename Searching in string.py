#Searching in string

text = "Python programming is fun."
substring = "programming"

try:
    position = text.index(substring)
    print(f"'{substring}' found at index {position}.")
except ValueError:
    print(f"'{substring}' not found.")