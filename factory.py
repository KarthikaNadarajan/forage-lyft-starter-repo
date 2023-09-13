from __future__ import annotations
from abc import ABC, abstractmethod
from car import Car
from datetime import date
from engine import *
from battery import *
class Creator(ABC):
    
    @abstractmethod
    def create_car(self):
        pass

    def check_car(self) -> str:
        # print("INSIDE CHECK CAR")
        car = self.create_car()
        # print("HEY ",car)
        return "Needs Service" if car.needs_service() else "Doesn't need service"
        
    
class Calliope(Creator):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage ) -> None:
        # print("INSIDE INIT Calliope")
        self.current_date=current_date
        self.last_service_date = last_service_date
        self.current_mileage= current_mileage
        self.last_service_mileage = last_service_mileage

    def create_car(self) -> Car:
        return Car(self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage,engine_cls=CapuletEngine,battery_cls=SpindlerBattery)

class Rorschach(Creator):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage ) -> None:
        # print("INSIDE INIT Rorschach")
        self.current_date=current_date
        self.last_service_date = last_service_date
        self.current_mileage= current_mileage
        self.last_service_mileage = last_service_mileage

    def create_car(self) -> Car:
        return Car(self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage,engine_cls=WilloughbyEngine,battery_cls=NubbinBattery)
    
class Glissade(Creator):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage ) -> None:
        # print("INSIDE INIT Glissade")
        self.current_date=current_date
        self.last_service_date = last_service_date
        self.current_mileage= current_mileage
        self.last_service_mileage = last_service_mileage

    def create_car(self) -> Car:
        return Car(self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage,engine_cls=WilloughbyEngine,battery_cls=SpindlerBattery)
    
class Palindrome(Creator):
    def __init__(self,current_date, last_service_date,  warning_light_on) -> None:
        # print("INSIDE INIT PALINDROME")
        self.current_date=current_date
        self.last_service_date = last_service_date
        self.warning_light_on = warning_light_on

    def create_car(self) -> Car:
        return Car(self.current_date, self.last_service_date,  warning_light_on=self.warning_light_on,engine_cls=SternmanEngine,battery_cls=SpindlerBattery)
    
class Thovex(Creator):
    def __init__(self,current_date, last_service_date, current_mileage, last_service_mileage ) -> None:
        # print("INSIDE INIT Thovex")
        self.current_date=current_date
        self.last_service_date = last_service_date
        self.current_mileage= current_mileage
        self.last_service_mileage = last_service_mileage

    def create_car(self) -> Car:
        return Car(self.current_date, self.last_service_date, self.current_mileage, self.last_service_mileage,engine_cls=CapuletEngine,battery_cls=NubbinBattery)
    
def client_code(creator: Creator) -> None:
    print(creator.check_car())
    
if __name__ == "__main__":
    print("App: Launched with the Palindrome")
    client_code(Palindrome(current_date=date(2023, 9, 12),last_service_date=date(2021, 9, 14) , warning_light_on=True))
    print("\n")
    print("App: Launched with the Thovex")
    client_code(Thovex(current_date=date(2023, 9, 12),last_service_date=date(2019, 9, 5) , current_mileage= 20000, last_service_mileage=15000 ))
    print("\n")
    print("App: Launched with the GLIssade")
    client_code(Glissade(current_date=date(2023, 9, 12),last_service_date=date(2021, 10, 5) , current_mileage= 50000, last_service_mileage=15000 ))
    print("\n")
