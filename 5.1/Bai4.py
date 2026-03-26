class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Hãng: {self.brand}")
        print(f"Mẫu: {self.model}")
        print(f"Năm: {self.year}")


class Car(Vehicle):  
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self): 
        super().display_info()
        print(f"Số cửa: {self.num_doors}")
        print("-" * 30)


class Bike(Vehicle):  
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type

    def display_info(self):  
        super().display_info()
        print(f"Loại xe: {self.type}")
        print("-" * 30)

if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020, 4)
    bike1 = Bike("Yamaha", "Exciter", 2021, "Sport")

    vehicles = [car1, bike1]

    for v in vehicles:
        v.display_info()