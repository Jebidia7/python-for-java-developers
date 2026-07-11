# This demonstrates Python's ability  to iterate over a collection
# while setting values from another collection also being iterated over

numbers = list((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))

# start at index 2, and go up to but excluding index 4
numbers[2:4] = (0, 0, 0, 0)
print(numbers)

# now remove all the elements starting at index 2, and up but excluding index 4
numbers[2:6] = []
print(numbers)

# start at index 1, go to the end of the list, with a step size of 2
numbers[1::2] = ["hello", "to", "you", "today"]
print(numbers)