import re # regex lib

text = "ID: 123 Some Corp. Serial: 345453"

result = re.match(r".*?(\d{3}).*?(\d*)$", text)


if result is None:
    print("No match")
else:
    print(result.group(1))
    # 123
    print(result.group(2))
    # 345453