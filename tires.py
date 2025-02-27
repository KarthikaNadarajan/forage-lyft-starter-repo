from abc import ABC, abstractmethod

class Tires(ABC):
    @abstractmethod
    def needs_service_tires(self) -> bool:
        pass

class CarriganTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service_tires(self):
        for tire in self.tire_wear:
            if tire >= 0.9:
                return True
        return False
    
class OctoprimeTires(Tires):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_service_tires(self):
        return sum(self.tire_wear) >= 3.0




