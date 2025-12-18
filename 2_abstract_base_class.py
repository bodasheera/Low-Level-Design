from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def start_engine(self): ...
    
    @abstractmethod
    def shift_gear(self): ...

    @abstractmethod
    def accelerate(self): ...

    @abstractmethod
    def brake(self): ...

    @abstractmethod
    def stop_engine(self): ...

class SportsCar(Car):

    def __init__(self, brand , model):
        self.brand = brand 
        self.model = model
        self.is_engine_on = False
        self.current_speed = 0
        self.current_gear = 0

    def start_engine(self):
        self.is_engine_on = True
        print("engine started")

    def shift_gear(self, gear):
        
        if not self.is_engine_on:
            print("engine is off ! cant shift gear")
        else:
            self.current_gear = gear 
            print(f"shifted to gear {self.current_gear}")

    def accelerate(self, speed):
        
        if not self.is_engine_on:
            print("engine is off ! cant accelerate")
        else:
            self.current_speed = speed 
            print(f"Accelerated {self.current_speed} km/hr")

    def brake(self):
        if not self.is_engine_on:
            print("engine is off ! cant brake")
        else:
            self.accelerate(0)
            self.shift_gear(1)

    def stop_engine(self):
        self.is_engine_on = False
        print("engine stopped")


c = SportsCar("mitsubishi", "lancer")
c.start_engine()
c.shift_gear(3)
c.accelerate(100)
c.brake()
c.stop_engine()
c.accelerate(100)
