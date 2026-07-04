# Unlike Java, functions cannot be overloaded and overridden
# Functions in Python get their "uniqueness" from their name (and package they belong to)
# Functions in Python can have default values, and they must come at the end of the args
def calculate_area(width, height, length= 1):
    # pass
    # allows it to compile w/o function being completed
    return width * height * length

area = calculate_area(2, 3)

print(area)