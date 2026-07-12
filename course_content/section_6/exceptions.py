try:
    dict = {}
    dict["hello"]

    print(1/0)
except ZeroDivisionError as ex:
    print("Failed:", ex)
except Exception as ex:
    print("Caught exception:", ex, type(ex))
finally:
    print("Finally")