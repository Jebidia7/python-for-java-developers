class Machine:
    def __init__(self):
        print("Machine is ready")

class Car(Machine):
    def __init__(self):
        super().__init__()
        print("Car is ready")

car = Car()