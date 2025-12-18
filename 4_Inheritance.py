

class Car():

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

    
    def accelerate(self):
        if(self.is_engine_on):
            self._current_speed += 20
            print(f"I show speed {self.current_speed} kms/hr")
        else:
            print("Turn on engine !")
      

    def brake(self): 
        if(self.is_engine_on):
            self._current_speed -= 20
            if self.current_speed < 0:
                self._current_speed = 0
            print(f"I show speed {self.current_speed} kms/hr")
        else:
            print("Turn on engine !")

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
    
    def change_gear(self):
        self._current_gear += 1
        print(f"Gear {self.current_gear}")

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


c = ManualCar("Suzuki", "Wagon R")
c.start_engine()
c.change_gear()
c.accelerate()
c.brake()
c.stop_engine()

print("\n")

c = ElectricCar("Tesla", "Model s")
c.start_engine()
c.charge_car()
c.accelerate()
c.brake()
c.stop_engine()