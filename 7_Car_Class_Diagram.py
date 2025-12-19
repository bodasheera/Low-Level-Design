"""
                    ┌────────────────────┐
                    │        Car         │
                    ├────────────────────┤
                    │ - brand : String   │
                    │ - model : String   │
                    │ - speed : int      │
                    ├────────────────────┤
                    │ + accelerate() : void │
                    │ + brake() : void      │
                    └────────────────────┘
                           ▲
               ┌───────────┴───────────┐
               │                       │
┌────────────────────────┐   ┌────────────────────────┐
│        ManualCar       │   │      ElectricCar        │
├────────────────────────┤   ├────────────────────────┤
│ ◆ gear : Gear          │   │ ◆ battery : Battery    │
└────────────────────────┘   └────────────────────────┘
         ◆│                          ◆│
          │                           │
   ┌──────────────┐           ┌──────────────┐
   │     Gear     │           │    Battery    │
   ├──────────────┤           ├──────────────┤
   │ - currentGear : int │    │ - capacity : int │
   ├──────────────┤           │ - chargeLevel : int │
   │ + changeGear() : void │  ├──────────────┤
   └──────────────┘           │ + charge() : void │
                               └──────────────┘

"""


class Car:

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self._speed = 0
        print(f"Car is {self.brand} {self.model}")

    def accelerate(self):
        self._speed = self.speed + 10
        print(f"Speed is {self.speed}")

    def brake(self):
        self._speed = self.speed - 10
        if self.speed < 0:
            self._speed = 0
        print(f"Speed is {self.speed}")

    @property
    def speed(self):
        return self._speed
    
    @property
    def model(self):
        return self._model
    
    @property
    def brand(self):
        return self._brand


        
class ManualCar(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self._gear = Gear(6)

    @property
    def gear(self):
        return self._gear

class ElectricCar(Car):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self._battery = Battery(10000)

    @property
    def battery(self):
        return self._battery
    
    def accelerate(self):
        super().accelerate()
        self._battery.discharge()
    
class Gear():

    def __init__(self, total_gears):
        self._current_gear = 0    
        self.total_gears = total_gears

    def change_gear(self, gear):
        if gear >= 0 and gear <= self.total_gears:
            self._current_gear = gear
            print(f"current gear is {self._current_gear}")
        else:
            print("Invalid gear")


class Battery():

    def __init__(self, battery_capacity):
        self._battery_capacity = battery_capacity
        self._battery_percentage = 100


    def charge(self):
        self._battery_percentage = 100
        print(f"Battery percentage is {self.battery_percentage}")

    def discharge(self):
        self._battery_percentage -= 5
        if self.battery_percentage < 0:
            self._battery_percentage = 0
        print(f"Battery percentage is {self.battery_percentage}")

    @property
    def battery_percentage(self):
        return self._battery_percentage


c = ManualCar('maruti', 'suzuki')    
c.gear.change_gear(1)
c.accelerate()
c.accelerate()
c.gear.change_gear(2)
c.accelerate()
c.brake()

print("\n")

e = ElectricCar('tesla', 'x')
e.accelerate()
e.accelerate()
e.accelerate()
e.accelerate()
e.battery.charge()