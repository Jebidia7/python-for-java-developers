class MyException(Exception):
    pass

try:
    raise MyException("Oops!")
except MyException as ex:
    print(ex)