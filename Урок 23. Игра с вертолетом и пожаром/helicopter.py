class Helicopter:
    def __init__(self, x, y, game_map):
        self.x = x
        self.y = y
        self.points = 0
        self.lives = 3
        self.water = 0
        self.tank_capacity = 1
        self.game_map = game_map

    def move(self, dy, dx):
        ny = self.y + dy
        nx = self.x + dx
        if 0 <= ny < len(self.game_map) and 0 <= nx < len(self.game_map[0]):
            self.y = ny
            self.x = nx
            print(f"🚁 Вертолет переместился на ({self.x}, {self.y})")

    def extinguish_fire(self, fire_manager):
        if (self.x, self.y) in fire_manager.fires:
            fire_manager.fires.remove((self.x, self.y))
            self.points += 10
            self.water -= 1
            self.game_map[self.y][self.x] = "empty"
            print("✅ Пожар потушен!")

    def refill_water(self):
        if self.game_map[self.y][self.x] == "river":
            self.water = self.tank_capacity
            print("💧 Вода пополнена из реки!")

    def visit_shop(self):
        print("🛒 Магазин улучшений:")
        print(f"1. Увеличить бак воды (+1), цена: {self.tank_capacity * 10} очков")
        choice = input("Выберите действие: ")
        if choice == "1" and self.points >= self.tank_capacity * 10:
            self.points -= self.tank_capacity * 10
            self.tank_capacity += 1
            print(f"🌊 Бак увеличен до {self.tank_capacity}")

    def visit_hospital(self):
        if self.game_map[self.y][self.x] == "hospital" and self.lives < 3:
            self.lives = 3
            print("🚑 Жизни восстановлены в госпитале!")