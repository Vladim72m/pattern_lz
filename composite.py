class File:
    def __init__(self, name):
        self.name = name

    def show(self, indent=""):
        print(f"{indent}- {self.name}")


class Folder:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, item):
        self.items.append(item)

    def show(self, indent=""):
        print(f"{indent}+ {self.name}")
        for item in self.items:
            item.show(indent + "  ")
