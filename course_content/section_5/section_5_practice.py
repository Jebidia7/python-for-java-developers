import re

def match(phrase):
    regex = re.compile(r"\bo\w+\S+", re.IGNORECASE)

    return {value: len(value) for i, value in enumerate(re.findall(regex, phrase))}

print(match("Oh, I wish Only it was Over tomorrow, Oi!"))
print(match("Oranges of Sicily are ordinarily on form"))

# FYI - the first prints as expected, the 2nd doesn't. Eff Regexes