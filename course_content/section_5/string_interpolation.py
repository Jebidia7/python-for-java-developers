distance = 1.23
height = 2.34

# This first example is the most recently "preferred" way of formating string outputs with vars
# Similar to Java's 'printf' (not the leading 'f' before the start of the string)
print(f"Height: {height:.1f}, Distance: {distance}")
# Height: 2.3, Distance: 1.23

# Slightly older way of doing the same
print("Height: {}, Distance: {}".format(height, distance))
# Height: 2.34, Distance: 1.23

# Same as above, but explicitly specifying the format args locations in the string
print("Height: {1:.1f}, Distance: {0}".format(distance, height))
# Height: 2.3, Distance: 1.23

# This will be prevalant in older code
print("Height: %.1f, Distance: %f" % (height, distance))
# Height: 2.3, Distance: 1.230000

# prefixing the string with 'r' ("raw string") will escape any special chars like the newline ('\n')
print(r"one\ntwo")
# one\ntwo