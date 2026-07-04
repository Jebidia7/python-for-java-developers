def calculate_area(width, height, length= 1):
    return width * height * length

# Python allows you to specify param names, and you can use them in any order
area = calculate_area(length=4, width=2, height=3)

print(area)

# can also mix and match - use some positional and some named 
area = calculate_area(4, length=2, height=3)