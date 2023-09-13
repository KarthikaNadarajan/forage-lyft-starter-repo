from car import Car
from datetime import date
from engine import *
from battery import *
from tires import *

class Creator():

    def __init__(self,engine,battery,tires) -> None:
        # print("inside init creator")
        self.__engine,self.__battery,self.__tires = engine,battery,tires

    def create_car(self):
        # print("inside create car")
        return Car(engine_cls=self.__engine,battery_cls=self.__battery,tire_cls= self.__tires)
    
    def check_car(self) -> str:
        # print("INSIDE CHECK CAR")
        car = self.create_car()
        return "Needs Service" if car.needs_service() else "Doesn't need service"
        
    
class Calliope(Creator):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> None:
        self.__engine = CapuletEngine(current_mileage, last_service_mileage)
        self.__battery = SpindlerBattery(current_date,last_service_date)
        self.__tires = CarriganTires(tire_wear)
        super().__init__(self.__engine,self.__battery,self.__tires)


class Rorschach(Creator):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> None:
        self.__engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.__battery = NubbinBattery(current_date,last_service_date)
        self.__tires = OctoprimeTires(tire_wear)
        super().__init__(self.__engine,self.__battery,self.__tires)  
    
class Glissade(Creator):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage, tire_wear) -> None:
        self.__engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.__battery = SpindlerBattery(current_date,last_service_date)
        self.__tires = CarriganTires(tire_wear)
        super().__init__(self.__engine,self.__battery,self.__tires) 

class Palindrome(Creator):
    def __init__(self, current_date, last_service_date, warning_light_on,  tire_wear) -> None:
        self.__engine = SternmanEngine(warning_light_on)
        self.__battery = SpindlerBattery(current_date,last_service_date)
        self.__tires = OctoprimeTires(tire_wear)
        super().__init__(self.__engine,self.__battery,self.__tires) 

    
class Thovex(Creator):
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage,  tire_wear) -> None:
        self.__engine = CapuletEngine(current_mileage, last_service_mileage)
        self.__battery = NubbinBattery(current_date,last_service_date)
        self.__tires = OctoprimeTires(tire_wear)
        super().__init__(self.__engine,self.__battery,self.__tires) 


def client_code(creator: Creator) -> None:
    print(creator.check_car())
    
if __name__ == "__main__":
    print("App: Launched with the Palindrome")
    client_code(Palindrome(current_date=date(2023, 9, 12),last_service_date=date(2021, 9, 14) , warning_light_on=False, tire_wear=[0.9,0,0.6,0.1] ))
    print("\n")
    print("App: Launched with the Calliope")
    client_code(Calliope(current_date=date(2023, 9, 12),last_service_date=date(2019, 9, 14) , current_mileage= 20000, last_service_mileage=15000, tire_wear=[0.9,0,0.6,0.1] ))
    print("\n")
    print("App: Launched with the Rorschach")
    client_code(Rorschach(current_date=date(2023, 9, 12),last_service_date=date(2019, 9, 5) , current_mileage= 50000, last_service_mileage=15000, tire_wear=[0.5,0.5,0.5,0.5] ))
    print("\n")
    print("App: Launched with the Glissade")
    client_code(Glissade(current_date=date(2023, 9, 12),last_service_date=date(2021, 9, 15) , current_mileage= 50000, last_service_mileage=15000, tire_wear=[0.5,0.5,0.5,0.5] ))
    print("\n")
