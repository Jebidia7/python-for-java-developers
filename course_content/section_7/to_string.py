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

person = Person("Mike")
person.eating()
print(person)

text = str(person)
print(text)