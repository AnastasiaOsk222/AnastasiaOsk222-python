import math

class Черепашка:
    def __init__(self, x=0, y=0, s=1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        # Движение вверх
        self.y += self.s
        print(f"Черепашка двинулась вверх. Текущая позиция: ({self.x}, {self.y})")

    def go_down(self):
        # Движение вниз
        self.y -= self.s
        print(f"Черепашка двинулась вниз. Текущая позиция: ({self.x}, {self.y})")

    def go_left(self):
        # Движение влево
        self.x -= self.s
        print(f"Черепашка двинулась влево. Текущая позиция: ({self.x}, {self.y})")

    def go_right(self):
        # Движение вправо
        self.x += self.s
        print(f"Черепашка двинулась вправо. Текущая позиция: ({self.x}, {self.y})")

    def evolve(self):
        # Увеличивает скорость на 1
        self.s += 1
        print(f"Скорость увеличена. Текущая скорость: {self.s}")

    def degrade(self):
        # Уменьшает скорость на 1, если она больше 1
        if self.s <= 1:
            raise ValueError("Скорость не может быть меньше или равна нулю.")
        self.s -= 1
        print(f"Скорость уменьшена. Текущая скорость: {self.s}")

    def count_moves(self, x2, y2):
        # Возвращает минимальное количество действий (ходов), за которое черепашка сможет добраться до точки (x2, y2)
        dx = abs(self.x - x2)
        dy = abs(self.y - y2)

        total_distance = dx + dy
        moves = math.ceil(total_distance / self.s)
        return moves

    def __str__(self):
        return f"Текущая позиция: ({self.x}, {self.y}), Скорость: {self.s}"


# Интерфейс с пользователем
def интерфейс():
    print("Добро пожаловать в управление черепашкой!")
    x = int(input("Введите начальную координату X: "))
    y = int(input("Введите начальную координату Y: "))
    s = int(input("Введите начальную скорость S: "))

    черепашка = Черепашка(x, y, s)

    while True:
        print("\n--- Меню ---")
        print("1. Вверх (↑)")
        print("2. Вниз (↓)")
        print("3. Влево (←)")
        print("4. Вправо (→)")
        print("5. Увеличить скорость")
        print("6. Уменьшить скорость")
        print("7. Посчитать ходы до точки")
        print("8. Показать текущее состояние")
        print("9. Выход")

        выбор = input("Выберите действие (1-9): ")

        try:
            if выбор == '1':
                черепашка.go_up()
            elif выбор == '2':
                черепашка.go_down()
            elif выбор == '3':
                черепашка.go_left()
            elif выбор == '4':
                черепашка.go_right()
            elif выбор == '5':
                черепашка.evolve()
            elif выбор == '6':
                черепашка.degrade()
            elif выбор == '7':
                x2 = int(input("Введите целевую координату X2: "))
                y2 = int(input("Введите целевую координату Y2: "))
                ходы = черепашка.count_moves(x2, y2)
                print(f"Минимальное число ходов до ({x2}, {y2}): {ходы}")
            elif выбор == '8':
                print(черепашка)
            elif выбор == '9':
                print("Выход из программы. До свидания!")
                break
            else:
                print("Неверный ввод. Попробуйте снова.")
        except ValueError as e:
            print("Ошибка:", e)


# Запуск программы
интерфейс()