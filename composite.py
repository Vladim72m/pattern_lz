# Вариант 4
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def show(self, indent=""): pass

class File(Component):
    def __init__(self, name):
        self.name = name

    def show(self, indent=""):
        print(f"{indent}- {self.name}")

class Folder(Component):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item: Component):
        self.items.append(item)

    def show(self, indent=""):
        print(f"{indent}+ {self.name}")
        for item in self.items:
            item.show(indent + "  ")
