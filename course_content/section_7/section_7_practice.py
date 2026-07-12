class Word:
    def __init__(self, word):
        self._word = word

    def __str__(self):
        return self._word

class AddableWord(Word):
    def __add__(self, other):
        return self._word + ":" + other._word

print(AddableWord('hello') + AddableWord('world'))
