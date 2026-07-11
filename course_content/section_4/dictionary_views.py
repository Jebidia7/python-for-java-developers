people = {
    "Bob": 42,
    "Sue": 53,
    "Steve": 25,
}

keys = people.keys()
values = people.values()
items = people.items()
print(keys)
# dict_keys(['Bob', 'Sue', 'Steve'])
print(values)
# dict_values([42, 53, 25])
print(items)
# dict_items([('Bob', 42), ('Sue', 53), ('Steve', 25)])

item_list = list(items)
print(item_list)
# [('Bob', 42), ('Sue', 53), ('Steve', 25)]

del people["Steve"]
print(items)
# dict_items([('Bob', 42), ('Sue', 53)])