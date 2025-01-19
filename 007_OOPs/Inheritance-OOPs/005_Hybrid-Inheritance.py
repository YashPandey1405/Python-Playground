class Vehicle:
    def __init__(self, brand, model):
        print("Vehicle Class Constructor Called....")
        self.brand = brand
        self.model = model

    def Display(self):
        print(f"Vehicle: Brand = {self.brand}, Model = {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        Vehicle.__init__(self, brand, model)  # Explicitly call Vehicle's constructor
        print("Car Class Constructor Called....\n")
        self.doors = doors

    def Display(self):
        Vehicle.Display(self)
        print(f"Car: Number of Doors = {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_capacity):
        Vehicle.__init__(self, brand, model)  # Explicitly call Vehicle's constructor
        print("Bike Class Constructor Called....\n")
        self.engine_capacity = engine_capacity

    def Display(self):
        Vehicle.Display(self)
        print(f"Bike: Engine Capacity = {self.engine_capacity}cc")

class ElectricCar(Car, Bike):
    def __init__(self, brand, model, doors, battery_capacity):
        Car.__init__(self, brand, model, doors)  # Explicitly call Car's constructor
        Bike.__init__(self, brand, model, None)  # Explicitly call Bike's constructor with None for engine_capacity
        print("ElectricCar Class Constructor Called....\n")
        self.battery_capacity = battery_capacity

    def Display(self):
        Car.Display(self)
        print(f"ElectricCar: Battery Capacity = {self.battery_capacity} kWh")

# Example Usage
obj = ElectricCar("Tesla", "Model S", 4, 100)
obj.Display()
