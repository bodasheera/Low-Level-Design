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
        self._is_engine_on = False
        self._current_speed = 0
        self._current_gear = 0
        self._tyre = "MRF"

    @property
    def is_engine_on(self):
        self._is_engine_on

    @property
    def current_speed(self):
        self._current_speed

    @property
    def current_gear(self):
        self._current_gear

    @property
    def tyre(self):
        return self._tyre
    
    @tyre.setter
    def tyre(self, tyre):
        self._tyre = tyre

    def start_engine(self):
        self._is_engine_on = True
        print("engine started")

    def shift_gear(self, gear):
        
        if not self.is_engine_on:
            print("engine is off ! cant shift gear")
        else:
            self._current_gear = gear 
            print(f"shifted to gear {self.current_gear}")

    def accelerate(self, speed):
        
        if not self.is_engine_on:
            print("engine is off ! cant accelerate")
        else:
            self._current_speed = speed 
            print(f"Accelerated {self._current_speed} km/hr")

    def brake(self):
        if not self.is_engine_on:
            print("engine is off ! cant brake")
        else:
            self.accelerate(0)
            self.shift_gear(1)

    def stop_engine(self):
        self._is_engine_on = False
        print("engine stopped")


c = SportsCar("mitsubishi", "lancer")
c.start_engine()
c.shift_gear(3)
c.accelerate(100)
c.brake()
c.stop_engine()
c.accelerate(100)

# basically add getters and no setters 
# make the property protected 
# should not be accesed as per consenting adult philosophy

# for tyre we added both getters and setters
print(c.tyre)
c.tyre = "Ceat"
print(c.tyre)