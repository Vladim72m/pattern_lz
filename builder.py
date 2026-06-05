# вариант 4 
from abc import ABC, abstractmethod

class Backpack:
    def __init__(self):
        self.contents = []  
class IBuilder(ABC): 
    @abstractmethod
    def add_parts(self): pass

class MathDayBuilder(IBuilder):
    def __init__(self):
        self.backpack = Backpack()
    
    def add_parts(self):
        self.backpack.contents.extend(["Учебник геометрии", "Тетрадь в клетку", "Циркуль", "Калькулятор"])
        return self.backpack

