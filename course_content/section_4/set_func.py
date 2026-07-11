numbers1 = {2, 4, 6, 7, 8, 9}
numbers2 = {2, 4, 6, 1, 3, 5}

print(numbers1.union(numbers2)) # mathematical union of the sets
# {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(numbers1.intersection(numbers2)) # mathematical intersection of the sets
# {2, 4, 6}

print(numbers1.difference(numbers2)) # removing the values from number1 that are in number2
print(numbers1 - numbers2)
# {8, 9, 7} for both

print(numbers2.difference(numbers1)) # removing the values from number2 that are in number1
print(numbers2 - numbers1)
# {1, 3, 5}

print(numbers1.symmetric_difference(numbers2)) # removing the mathematical intersection of the two sets (i.e., XOR)
# {1, 3, 5, 7, 8, 9}

print({1, 2, 3}.issuperset({1, 2, 3})) # A mathematical superset of a set, is a set that contains all the elements of another set
# True
print({1, 2, 3, 4, 5}.issuperset({1, 2, 3}))
# True
print({1, 2, 3}.issuperset({1, 2, 3, 4}))
# False