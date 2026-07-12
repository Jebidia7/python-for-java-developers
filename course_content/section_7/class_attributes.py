# class attributes ~= static variables in Java
class Machine:

    count = 0 # NOT an instance var when declared like this

    def __init__(self):
        Machine.count += 1

Machine()
Machine()
Machine()

print(Machine.count)