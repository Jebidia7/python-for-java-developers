# and, not, or
# True, False

raining = False
temperature = 75

if temperature > 80 and not raining:
    print("Weather fine")
elif not raining:
    print("At least it's dry")
else:
    print("It's raining. Stay inside")

mood = "good" if not raining else "bad"
print(mood)