class A:
    def run(self):
        print("Hello from 'A'")

class B:
    def run(self):
        print("Hello from 'B'")

# The order in which methods are resolved are as follows:
# 1. It checks the class itself, i.e., 'C'
# 2. Then it checks the classes inherited in the order they're listed at the class definition
#    In this case, it'll check 'A' first, and then 'B', and so on
# 3. Finally, it will look at the 'object' superclass (similar to Java's Object class that everything inherits from)
class C(A, B):
    pass

c = C()
c.run()

print(C.mro())
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]