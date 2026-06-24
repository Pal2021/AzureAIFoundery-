class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
    def get_description(self):
        return f"{self.__year} {self.__make} {self.__model}"

class ElectricCar(Car):
    def __init__(self,make,model,year,battery_size):
        super().__init__(make,model,year)
        self.battery_size=battery_size

    def get_description(self):
        return f"{self.__year} {self.__make} {self.__model} with a {self.battery_size}-kWh battery"

# print("Car class defined successfully.")
get_car=ElectricCar("Tesla","Model S",2022,100)
print(get_car.model)
# print(get_car.get_description())