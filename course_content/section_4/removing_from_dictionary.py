days = {
    "Mon":"Monday",
    "Tue":"Tuesday",
    "Wed":"Wednesday",
    "Thur":"Thursday",
    "Fri":"Friday",
    "Sat":"Saturday",
    "Sun":"Sunday",
}

del days["Mon"]
print(days)
# {'Tue': 'Tuesday', 'Wed': 'Wednesday', 'Thur': 'Thursday', 'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday'}

print(days.pop("Thur"))
# Thursday

print(days.popitem()) # removes last item (as a tuple)
# ('Sun', 'Sunday')
print(days)
# {'Tue': 'Tuesday', 'Wed': 'Wednesday', 'Fri': 'Friday', 'Sat': 'Saturday'}

# in either case days will be an empty dictionary
days.clear()
days = {}
print(days)
print(type(days))