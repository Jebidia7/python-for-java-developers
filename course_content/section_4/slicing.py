animals = ("dog", "cat", "bird", "horse", "pig", "tiger", "bear", "fish")
for animal in animals:
    print(animal)

print(animals[2]) # "slice" of the animals tuple
print(animals[1:4]) # get indexes at 1, 2, and 3 (up to, but not including '4')
print(animals[-1]) # get the last item in the tuple
print(animals[-4:-1])
print(animals[1:-1:2]) # third item is step size (i.e., the number "2")
print()
# All 3 below produce the same results based on default values in the range
print(animals)
print(animals[:])
print(animals[::])

# [<start>:<end_exclusive>:<step>]