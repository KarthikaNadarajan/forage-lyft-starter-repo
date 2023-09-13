from __future__ import annotations
from abc import ABC, abstractmethod
from engine import Engine
from datetime import date
from battery import Battery

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    def __init__(self,current_date: date, last_service_date: date, current_mileage: int=0, last_service_mileage: int=0,  warning_light_on: bool = False,engine_cls:Engine=None,battery_cls:Battery = None) -> None:
        self.__engine = engine_cls(current_mileage, last_service_mileage, warning_light_on)
        self.__battery = battery_cls(current_date,last_service_date)
        # print("INIT CAR ")

    
    def needs_service(self) -> bool:
        # print("Inside needs_service of Car ")
        return self.__engine.needs_service_engine() or self.__battery.needs_service_battery()
    
