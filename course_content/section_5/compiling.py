import re

text = "dog cat mouse"

# flags need to be provided in the compile method if being used
regex = re.compile(r"C.*T", flags=re.IGNORECASE)
result = re.sub(regex, "giraffe", text)

print(result)