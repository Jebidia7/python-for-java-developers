class Person:

    ##############################################################
    # Note: No properties need to be defined here in Python classes
    ##############################################################

    # class constructor
    # double-underscore methods also called "Dunder" methods
    # Dunder methods considered "private" (though, just by naming convention only)
    def __init__(self, name):
        # internal properties of a class are prefixed with a single underscore by Python conventions
        self._name = name

    # self ~= this in Java
    def eating(self):
        print(f"{self._name} eating!")


person = Person("Mike")
person.eating()
print(person)