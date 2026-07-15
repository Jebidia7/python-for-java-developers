animals = ["dog", "giraffe", "elephant", "tiger", "lion"]

# default alphabetically
sortedAnimals = sorted(animals)
print(sortedAnimals)
# ['dog', 'elephant', 'giraffe', 'lion', 'tiger']

# reverse order
sortedAnimals = sorted(animals, reverse=True)
print(sortedAnimals)
# ['tiger', 'lion', 'giraffe', 'elephant', 'dog']

# use lambda to provide custom sorting, in this case by length
sortedAnimals = sorted(animals, reverse=True, key=lambda s: len(s))
print(sortedAnimals)
# ['elephant', 'giraffe', 'tiger', 'lion', 'dog']