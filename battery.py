from abc import ABC, abstractmethod

class Battery(ABC):
    @abstractmethod
    def needs_service_battery(self) -> bool:
        pass

class SpindlerBattery(Battery):
    def __init__(self,current_date,last_service_date) -> None:
        self.current_date = current_date
        self.last_service_date = last_service_date
        
    def needs_service_battery(self) -> bool:
        # print(self.last_service_date.replace(year = self.last_service_date.year + 2))
        if self.current_date > self.last_service_date.replace(year = self.last_service_date.year + 3):
            return True
        else:
            return False


class NubbinBattery(Battery):
    def __init__(self,current_date,last_service_date) -> None:
        self.current_date = current_date
        self.last_service_date = last_service_date
        
    def needs_service_battery(self) -> bool:
        if self.current_date > self.last_service_date.replace(year = self.last_service_date.year + 4):
            return True
        else:
            return False