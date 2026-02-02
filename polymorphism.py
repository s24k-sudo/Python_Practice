class Vehicle:
    def __init__(self,brand , model, year):
        self.brand=brand
        self.model=model
        self.year=year

    def start(self):
        print("vehicle is started")
    
    def stop(self):
        print("stpooed")

class Car (Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand,model,year)
        self.brand=brand
        self.model=model
        self.year=year
        self.number_of_doors=number_of_doors
    def start(self):
        print("The car is starting")

    def stop(self):
       print("The car is stopping")


class Motercycle(Vehicle):
    def __init__(self,brand, model, year):
        super().__init__(brand,model,year)
        self.brand=brand
        self.model=model
        self.year=year
    
    def start(self):
        print("The motercycle is starting")

    def stop(self):
        print("The motercycle is stopping")

class Plane(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("The plane  is taking off..")

    def stop(self):
        print("The plane is landing..")

   


vehicles: list[Vehicle] = [
    Car("Tata", "Sieara", 2026, 5),
    Motercycle("Royel Enfield", "Classic", 2018),
    Plane("Boying771","Air India ",2016)
]
#loop through the vehicle list and inspect them
for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand}{vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("The object not found")

    
    

