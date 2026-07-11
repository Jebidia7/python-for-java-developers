numbers = {1, 4, 2, 7, 3, 0}
print(numbers)

for number in numbers: # sets don't come out in a predictable order
    print(number)

print(3 in numbers)
# True

numbers.add(7)
print(numbers)

numbers.update([9, 8])
print(numbers)
# {0, 1, 2, 3, 4, 7, 8, 9}

numbers.remove(1) # sets don't have any indexes because it's not a fixed order
print(numbers)

numbers.discard(10) # discard prevents a traceback (i.e., like Java's "runtime exception") if the item doesn't exist
print(numbers)

print(set([1, 2, 3])) # creates a set from a list
print({n for n in range(5,8)}) # set generated from a comprehension