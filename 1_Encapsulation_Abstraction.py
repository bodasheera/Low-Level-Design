
class Car:

    def __init__(self, brand , model):
        self.brand = brand
        self.model = model
        self.isEngineOn = False

    def start(self):
        self.isEngineOn = True

    def stop(self):
        self.isEngineOn = False

    def shift_gear(self):
        ...

    def accelerate(self):
        ...
        
class Owner:

    def __init__(self, name: str, car: Car):
        self.name = name
        self.car = car

    def drive(self):
        self.car.start()
        self.car.shift_gear()
        self.car.accelerate()


# Basically objects interact with each other 
