class Word:
    def __init__(self, text):
        self._text = text

    def __str__(self):
        return self._text

    def __add__(self, other):
        return Word(self._text + other._text)

w1 = Word("Hello")
w2 = Word("World")
# the '+' operator uses "__add__()" under the hood
print(w1 + w2)