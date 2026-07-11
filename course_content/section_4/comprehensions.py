numbers = [i for i in range(0, 5)]
print(numbers)
# [0, 1, 2, 3, 4]

numbers = [i**2 for i in range(0, 5)]
print(numbers)
# [0, 1, 4, 9, 16]

animals = ["cat", "mouse", "dog", "badger"]

animals2 = [animal for animal in animals]
print(animals2)

lengths = [len(animal) for animal in animals]
print(lengths)
# [3, 5, 3, 6]