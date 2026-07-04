def details(name, **kwargs): # "**" syntax to define "kwargs" as type dict (similar to hashmap in Java)
    print("Name", name)

    print(type(kwargs))
    print(kwargs)

    if "height" in kwargs:
        print("Height", kwargs["height"])

    for key in kwargs:
        print(key, kwargs[key])

details("Sue", height=60, weight=80)
details("Sue", height2=70, weight=80)
