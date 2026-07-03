value = 11

match value:
    case 10|11: # matches for 10 OR 11
        print("OK")
    case 15:
        print("Warning")
    case _:
        print("Unknown code")