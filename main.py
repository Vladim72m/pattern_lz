# Вариант 4
from builder import MathDayBuilder, Director
from composite import File, Folder
from command import Light, Command, Button

def main():
    builder = MathDayBuilder()
    director = Director(builder)

    director.build_full_pack()
    backpack = builder.get_result()
    print(backpack)

    print("Компоновщик:")
    file1 = File("document.txt")
    file2 = File("photo.png")

    root = Folder("Главная папка")
    subfolder = Folder("Вложенная папка")

    subfolder.add(file2)
    root.add(file1)
    root.add(subfolder)

    root.show()

    print("Команды от кнопок:")
    light = Light()

    btn_on = Button("Включить свет", Command(light, "on"))
    btn_break = Button("Сломать лампу", Command(light, "break_lamp"))

    btn_on.click()
    btn_break.click()
    btn_on.click()


if __name__ == "__main__":
    main()
