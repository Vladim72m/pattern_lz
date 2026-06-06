class Backpack:
    def __init__(self):
        self.contents = []
        self.food = None
        self.water = None

    def __str__(self):
        result = "Рюкзак:\n"
        for item in self.contents:
            result += f"- {item}\n"
        result += f"Еда: {self.food if self.food else 'нет'}\n"
        result += f"Вода: {self.water if self.water else 'нет'}\n"
        return result


class BackpackBuilder:
    def add_books(self):
        pass
    def add_tools(self):
        pass
    def add_food(self):
        pass
    def add_water(self):
        pass
    def get_result(self) -> Backpack:
        pass


class MathDayBuilder(BackpackBuilder):
    def __init__(self):
        self.backpack = Backpack()

    def add_books(self):
        self.backpack.contents.append("Учебник геометрии")
        self.backpack.contents.append("Тетрадь в клетку")

    def add_tools(self):
        self.backpack.contents.append("Циркуль")
        self.backpack.contents.append("Линейка")
        self.backpack.contents.append("Калькулятор")

    def add_food(self):
        self.backpack.food = "Бутерброд"

    def add_water(self):
        self.backpack.water = "Бутылка воды"

    def get_result(self) -> Backpack:
        return self.backpack

class Director:
    def __init__(self, builder: BackpackBuilder = None):
        self.builder = builder

    def build_minimal_pack(self):
        self.builder.add_books()
        self.builder.add_tools()

    def build_full_pack(self):
        self.builder.add_books()
        self.builder.add_tools()
        self.builder.add_food()
        self.builder.add_water()
          
