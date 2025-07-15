import random

class FireManager:
    def __init__(self, game_map):
        self.game_map = game_map
        self.fires = []

    def update_fires(self, game_map, heli):
        # Принудительное появление пожара для теста
        if not self.fires:
            print("🔥 Тест: создаём первый пожар в случайном месте")
            x, y = random.randint(0, len(game_map[0])-1), random.randint(0, len(game_map)-1)
            if game_map[y][x] == "tree":
                self.fires.append((x, y))
                print(f"🔥 Появился пожар в ({x}, {y})")

        # Обычное появление новых пожаров
        if random.random() < 0.9:
            x, y = random.randint(0, len(game_map[0])-1), random.randint(0, len(game_map)-1)
            if game_map[y][x] == "tree" and (x, y) not in self.fires:
                self.fires.append((x, y))
                print(f"🔥 Новый пожар в точке ({x}, {y})")

        # Распространение огня
        new_fires = []
        for (x, y) in self.fires:
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(game_map[0]) and 0 <= ny < len(game_map):
                    if game_map[ny][nx] == "tree" and (nx, ny) not in self.fires:
                        new_fires.append((nx, ny))
        self.fires.extend(new_fires)

        # Удаление сгоревших деревьев
        to_remove = []
        for (x, y) in self.fires:
            if random.random() < 0.05:  # Чуть чаще
                game_map[y][x] = "empty"
                to_remove.append((x, y))
                heli.lives -= 1
                print(f"🌲 Дерево сгорело в ({x}, {y}), потеряно 1 жизнь")

        for pos in to_remove:
            if pos in self.fires:
                self.fires.remove(pos)