
value = 7

try:
    assert value > 8, "Oops!"
except AssertionError as ae:
    print(ae)

# assert False, "Oops! Should be True"