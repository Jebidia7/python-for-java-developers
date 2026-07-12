import re # regex lib

text = r"a\nz"

# Even though working with raw string, with the regex engine you need to escape '\n' still
result = re.match(r"a\\nz", text)

# Ternary operator
print("No match" if result is None else result.group())