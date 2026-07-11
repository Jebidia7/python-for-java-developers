fruits = ["apple", "orange", "grape"]

print(id(fruits))
fruits += ["melon"]
print(id(fruits)) # since 'fruits' is a list (not a tuple), and lists are mutable, the id/memory location remains the same

print(fruits)

fruits[0] = "strawberry"
print(fruits)

fruits.append("pear")
print(fruits)

fruits.extend(["blueberry", "pineapple"])
print(fruits)

fruits.insert(2, "kiwi")
print(fruits)

fruits_tuple = tuple(fruits) # create tuple from the list
print(fruits_tuple)

fruits_list = list(fruits_tuple) # create list from the tuple
print(fruits_list)