import re

tag = r'<div id="123">Hello</div>'
print(tag)

result = re.match(
    r"""
        <div\s+  # Match opening tag
        id="(\d+)" # Match ID
        >  # Match closing tag
        ([^<>]+) # Get content between open and closing tag
        </div>
    """,
    tag, re.VERBOSE)

# groups() returns a Tuple of the capture groups that matched
print("No match" if result is None else result.groups())
# ('123', 'Hello')