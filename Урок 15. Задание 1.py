# Определение родительского класса Transport
class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Создание дочернего класса Autobus
class Autobus(Transport):
    pass  # Все методы и атрибуты наследуются от Transport

# Создание объекта Autobus
bus = Autobus("Renaul Logan", 180, 12)

# Вывод информации
print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")