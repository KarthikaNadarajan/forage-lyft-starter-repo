from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def needs_service_engine(self) -> bool:
        pass

class CapuletEngine(Engine):
    def __init__(self,current_mileage, last_service_mileage) -> None:
        # print("IN CAPULET ENGINE INIT")
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def needs_service_engine(self) -> bool:
        # print("IN CAPULET ENGINE needs_service_engine")
        return self.current_mileage - self.last_service_mileage > 30000


class WilloughbyEngine(Engine):
    def __init__(self,current_mileage, last_service_mileage) -> None:
        # print("IN  WilloughbyEngine ENGINE INIT")
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        
    def needs_service_engine(self) -> bool:
        # print("IN  WilloughbyEngine needs_service_engine")
        return self.current_mileage - self.last_service_mileage > 60000
    
class SternmanEngine(Engine):
    def __init__(self,warning_light_is_on=False) -> None:
        self.warning_light_is_on = warning_light_is_on

    def needs_service_engine(self) -> bool:
        if self.warning_light_is_on:
            return True
        else:
            return False   


