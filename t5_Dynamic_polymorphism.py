from abc import ABC, abstractmethod

class Car(ABC):

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._current_speed = 0
        self._is_engine_on = False
        print(f"{self.brand} {self.model}")
        
    def start_engine(self):
        if self.is_engine_on:
            print("Engine is already on !")
        self._is_engine_on = True
        print("Engine turned on !")

    @abstractmethod
    def accelerate(self): ...
      
    @abstractmethod 
    def brake(self): ...

    def stop_engine(self):
        self._is_engine_on = False
        print("Engine turned off !")

    @property
    def current_speed(self):
        return self._current_speed
    
    @property
    def is_engine_on(self):
        return self._is_engine_on

class ManualCar(Car):

    def __init__(self, brand , model):
        super().__init__(brand, model)
        self._current_gear = 0

    @property
    def current_gear(self):
        return self._current_gear
    
    def change_gear(self, gear):
        self._current_gear = gear
        print(f"Gear {self.current_gear}")

    def accelerate(self):
        if self.is_engine_on:
            self._current_speed += 20
        print(f"I show speed {self.current_speed} kms/hr")


    def brake(self):
        self.change_gear(0)
        self._current_speed -= 20

class ElectricCar(Car):

    def __init__(self, brand , model):
        super().__init__(brand, model)
        self._battery_percentage = 100

    @property
    def battery_percentage(self):
        return self._battery_percentage
    
    def charge_car(self):
        self._battery_percentage = 100
        print(f"battery charged to {self.battery_percentage}")

    def accelerate(self):
        if self.is_engine_on:
            self._current_speed += 15
            self._battery_percentage -= 10
        print(f"I show speed {self.current_speed} kms/hr. Battery is {self.battery_percentage}")

    def brake(self):
        self._current_speed -= 15
        print(f"I show speed {self.current_speed} kms/hr") 


c = ManualCar("Suzuki", "Wagon R")
c.start_engine()
c.change_gear(2)
c.accelerate()
c.brake()
c.stop_engine()

print("\n")

c = ElectricCar("Tesla", "Model s")
c.start_engine()
c.charge_car()
c.accelerate()
c.accelerate()
c.accelerate()
c.brake()
c.stop_engine()