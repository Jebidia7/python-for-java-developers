functions = []

# There's only a single 'i' variable, and that will get updated
# as the loop executes
for i in range(5):
    functions.append(lambda: print(i))

for f in functions:
    f()
# prints out '4' 5 times

# This 'fixes' it by telling the lambda to declare a var 'i' and set it to
# the loop's 'i', and then use that [inner]'i' for the print function
for i in range(5):
    functions.append(lambda i= i: print(i))

for f in functions:
    f()
# prints out 0 - 4 as you expect