def names():
    return "Mike", "Jay", "Danny"

my_names = names()

print(type(my_names)) # "names" is a tuple
print(my_names)

name1, name2, name3 = names() # This is almost similar to Elixir's and JS's object destructuring 
print(name1, name2, name3)