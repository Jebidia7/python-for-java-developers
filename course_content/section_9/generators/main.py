# looks like tuple-comprehension, but this returns a generator
letters = (chr(x) for x in range(65, 91))

# This cast to list will create the entire list before printing
# print(list(letters))

# iterating through the generator will only produce the items one by one
for s in letters:
    print(s, end=" ")