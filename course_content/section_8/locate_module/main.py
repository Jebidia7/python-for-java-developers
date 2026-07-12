import sys
import stuff.greetings as gr

# print("\n".join(sys.path))
# print("Greetings file:", gr.__file__) # this only works with modules that are actual files

value = 7
print("\n".join(dir(gr)))
print("\n".join(dir(sys)))
