class Vehicle:
 
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
 
    def get_info(self):
        return f"brand: {self.brand}, model:{self.model} , year:{self.year}"
 
 
class Car(Vehicle):
 
    def __init__(self,brand,model,year,number_of_doors):
        super().__init__(brand, model , year)
        self.number_of_doors = number_of_doors
 
    def get_info(self):
        return f"brand: {self.brand}, model: {self.model} , year: {self.year}, Doors: {self.number_of_doors}"
   
myCar = Car("Toyota","Prius", 2022 , 5)
print(myCar.get_info())