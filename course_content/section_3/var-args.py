def catalogue(name, *args): # "*" prefix for var-args variable

    print("Type: ", type(args)) # "args" is of type tuple

    print(name)

    if len(args) >= 1:
        print(args[0])

    for arg in args:
        print(arg)

catalogue("Trees", "oak", "pine", "maple")

catalogue("MN Trees")