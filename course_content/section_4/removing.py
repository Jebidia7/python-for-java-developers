numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.remove(4) # remove element that matches number 4
print(numbers)

value = numbers.pop(1) # pop at index 1
print(value)
print(numbers)

del numbers[2]
print(numbers)

numbers.clear()
print(numbers)