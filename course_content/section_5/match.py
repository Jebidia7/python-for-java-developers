import re # regex module

text = "Once upon a time"

result = re.match(r"o.*?", text, flags=re.IGNORECASE)
print(result)

# The 'is' keyword is Python's way of checking whether two object IDs are the same
# 'None' is a special singleton object in Python which is equivalent to 'null' in Java
# However 'null' in Java represents an empty pointer, whereas 'None' in Python has an address
if result is None:
    print("No match")
else:
    print(result.group())
    # O