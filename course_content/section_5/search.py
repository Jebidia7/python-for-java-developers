import re

text = """
one
two
three
"""

# re.DOTALL will match everything including the [hidden] '\n' characters
result = re.search(r"(t.*e)", text, re.DOTALL)

print("No match" if result is None else result.groups())
# ('two\nthree',)