# "Container" in Python is synonymous with "Collection" in Java
stuff = ("Mike", 45, 9.5, True, False, "Cats") # "packing" the tuple

print(stuff[2])
# stuff[2] = True # Tuples are immutable

name, age, height, thick, straight, pets = stuff # "unpacking" the tuple
print(name)
print(age)
print(height)
print(thick)

person, number1, number2, *other = stuff # "unpacking" the tuple, with "other" containing remainder of tuple
print(person, number1, number2, *other)
print(type(other)) # "other" is of type List