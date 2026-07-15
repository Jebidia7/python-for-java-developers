def greet():
    print("Hello!")

def run(func): # doesn't have to be 'func', just needs to be a callable because of our function implementation
    func()

run(greet)