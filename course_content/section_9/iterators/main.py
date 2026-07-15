class PowersOfTwo:

    # called once to get the iterable
    def __iter__(self):
        self._value = 1
        return self

    # called for each item
    def __next__(self):

        self._value *= 2

        if self._value > 20:
            raise StopIteration

        return self._value

for i in PowersOfTwo():
    print(i)