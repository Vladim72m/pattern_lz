# Вариант 4 

class Light:
    def __init__(self):
        self.is_broken = False

    def on(self):
        if self.is_broken:
            print("Свет выключен.")
        else:
            print("Свет включен.")

    def break_lamp(self):
        self.is_broken = True


class Command:
    def __init__(self, receiver, action):
        self.receiver = receiver
        self.action = action

    def execute(self):
        getattr(self.receiver, self.action)()


class Button:
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def click(self):
        print(f"[Нажата кнопка '{self.name}']")
        self.command.execute()
        # Вариант 4 

class Light:
    def __init__(self):
        self.is_broken = False

    def on(self):
        if self.is_broken:
            print("Свет выключен.")
        else:
            print("Свет включен.")

    def break_lamp(self):
        self.is_broken = True


class Command:
    def __init__(self, receiver, action):
        self.receiver = receiver
        self.action = action

    def execute(self):
        getattr(self.receiver, self.action)()


class Button:
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def click(self):
        print(f"[Нажата кнопка '{self.name}']")
        self.command.execute()
        
