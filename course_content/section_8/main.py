from my_other_module import value, other_value # when you want to import individual "things" and not the entire module

# import stuff.greetings as gr
# from stuff import greetings as gr
from stuff.greetings import  greet

# gr.greet()
greet()

print(value)
print(other_value)

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()

