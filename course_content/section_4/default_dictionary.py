from collections import defaultdict

people = {
    "Bob": 42,
    "Sue": 53,
    "Steve": 25,
}

print(people.get("Mike", 45))
# 45 - because 'Mike' doesn't exist in the dict

days = defaultdict(str)

days.update({"Mon": "Monday", "Tue": "Tuesday", "Wed": "Wednesday"})

print(days)
# defaultdict(<class 'str'>, {'Mon': 'Monday', 'Tue': 'Tuesday', 'Wed': 'Wednesday'})
print(days["Mon"])
# Monday
print(days["Thr"]) # default value of our dict is an empty string
# "" (empty string)
