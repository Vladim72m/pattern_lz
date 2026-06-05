# Вариант 4
from builder import ComputerBuilder
from composite import Folder, File
from command import Light, OnCommand, Remote

def main():
    # 1. Строитель
    comp = ComputerBuilder().add_parts()
    print("Сборка ПК:", comp.parts)

    # 2. Компоновщик
    root = Folder("Корень")
    root.add(File("doc.txt"))
    root.show()

    # 3. Команда
    light = Light()
    remote = Remote()
    remote.cmd = OnCommand(light)
    remote.press()

if __name__ == "__main__":
    main()
