# in Python it has to be immutable to create a hash from

# print(hash([1,2,3])) # error

print(hash((1,2,3))) # error

print(hash((1,2,[]))) # also error because list is mutable even though tuples are immutable