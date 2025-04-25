
import re

pattern = r"^Hello, world!$"  # ^ indicates start of string, $ indicates end of string

# The string to match
text = "Hello, world!"

# Using fullmatch to check if the entire string matches the pattern
if re.fullmatch(pattern, text):
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")