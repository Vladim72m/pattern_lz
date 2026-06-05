# Вариант 4
from abc import ABC, abstractmethod

class Light:
    def turn_on(self): print("Свет горит")
    def turn_off(self): print("Свет погас")

class ICommand(ABC):  
    @abstractmethod
    def execute(self): pass

class OnCommand(ICommand):
    def __init__(self, light): self.light = light
    def execute(self): self.light.turn_on()

class OffCommand(ICommand):
    def __init__(self, light): self.light = light
    def execute(self): self.light.turn_off()

class Remote:
    def __init__(self): self.cmd = None
    def press(self): self.cmd.execute()
