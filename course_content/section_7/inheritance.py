class Person:
    # class constructor
    # double-underscore methods also called "Dunder" methods
    # Dunder methods considered "private" (though, just by naming convention only)
    def __init__(self, name):
        # internal properties of a class are prefixed with a single underscore by Python conventions
        self._name = name

    # self ~= this in Java
    def eating(self):
        print(f"{self._name} is eating!")

    # Python's equivalent of overriding Java's Object.toString(); method
    def __str__(self):
        return f"Hello I am {self._name}"

    # Purpose of __repr__ is a "string representation" for the machine (not the human)
    # and doing "eval(repr(obj))" Python can use the output to actually run the code
    def __repr__(self):
        return f'Person("{self._name}")'

# Employee extends Person
class Employee(Person):

    def go_on_holiday(self):
        print(f"{self._name} is going on holiday!")

person = Person("Mike")
e = Employee("Matt")
e.eating()
e.go_on_holiday()
