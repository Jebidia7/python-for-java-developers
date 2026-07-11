fruits = ("apple",) # needs the ',' at the end otherwise it'll create a string and not a tuple
days = ["mon"] # list
names = {"Mike"} # set
months = {"Jan":"January",} # dict

something = [
    {1,2,3},
    {
        8: "eight",
        9: (9,)
    }
]

print(something)
# [{1, 2, 3}, {8: 'eight', 9: (9,)}]