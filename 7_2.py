class Vehicle:
    def __init__(self, make):
        self.make = make

    def description(self):
        print(f"Make: {self.make}")

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make)
        self.model = model

    def description(self):
        super().description()
        print(f"Model: {self.model}")

class ElectricCar(Car):
    def __init__(self,make, model, battery_size):
        super().__init__(make, model)
        self.battery_size = battery_size

    def description(self):
        super().description()
        print(f"Battery Size: {self.battery_size}")

v = Vehicle("Vin fet")
v.description()
c = Car("Toyota", "JAV3")
c.description()
ec = ElectricCar("Four", "everest",100000)
ec.description()
