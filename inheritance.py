class Vehicle:
    def __init__(self, brand, model , year):
        self.brand=brand
        self.model=model
        self.year=year

    def start(self):
        print("Vehicle is starting......")
    
    def stop(self):
        print("Vehicle is stopped.......")


class car (Vehicle):
    def __init__(self, brand, model, year, number_of_wheels, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors=number_of_doors
        self.numbr_of_wheels=number_of_wheels

class bike (Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels =number_of_wheels


car1 = car("Tata","Sieara",2026,5,4)
bike1= bike("Royal Enfild","Classicc350",2018,2)
car1.start()
print(car1.__dict__)
car1.stop()
bike1.start()
print(bike1.__dict__)
bike1.stop()