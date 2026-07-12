class Animal:
    def speak(self):
        print("I am an Animal")

class Cat(Animal):
    def speak(self):
        print("Meow!")

cat = Cat()
cat.speak()