months = { # Like a Map in Java
    "Jan":"January",
    "Feb":"February",
    "Mar":"March", # you can leave this trailing comma and it's still syntactically correct
}

print(months["Jan"])
# January

months["Apr"] = "April"
print(months)
# {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April'}

months.update({ "May":"May", "Jun":"June", "Jul":"July"})
print(months)
# {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April', 'May': 'May', 'Jun': 'June', 'Jul': 'July'}

for month in months: # similar to 'for month in months.keys()'
    print(month, months[month])

for month in months.values():
    print(month)

for month in months.items(): # similar to Java's Entry<K,V>
    print(month)
# prints out entries as individual tuples

for abbrv, name in months.items():
    print(abbrv, name)
# prints out entries as strings, (e.g., "May May", "Jan January" etc.)

print("Jan" in months)
# True

print("Oct" in months)
# False