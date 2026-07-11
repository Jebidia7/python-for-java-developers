fruits = ("apple", "banana", "cherry")
days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")

for i, fruit in enumerate(fruits):
    print(i, fruit)
# 1 apple
# 2 banana
# 3 cherry

for fruit, days in zip(fruits, days):
    print(fruit, days)
# apple Mon
# banana Tue
# cherry Wed
# note, it skips the rest of the days tuple because fruits tuple is smaller in count