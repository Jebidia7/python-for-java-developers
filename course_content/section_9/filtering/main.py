fruits = ["apple", "orange", "banana", "grapes", "pear"]

filteredFruits = filter(lambda s: "e" in s, fruits)
print(list(filteredFruits))
# ['apple', 'orange', 'grapes', 'pear']