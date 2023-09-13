from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
from tires import Tires

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    def __init__(self,engine_cls:Engine=None,battery_cls:Battery = None, tire_cls : Tires=None) -> None:
        self.__engine = engine_cls
        self.__battery = battery_cls
        self.__tires = tire_cls
        # print("INIT CAR ")
    
    def needs_service(self) -> bool:
        # print("Inside needs_service of Car ")
        return self.__engine.needs_service_engine() or self.__battery.needs_service_battery() or self.__tires.needs_service_tires()
    
