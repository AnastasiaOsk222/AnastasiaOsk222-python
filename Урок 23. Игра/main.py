import time
from helicopter import Helicopter
from fire_manager import FireManager
from map_generator import MapGenerator
from utils import save_game, load_game

def print_map(game_map, heli):
    symbols = {
        "empty": " . ",
        "tree": " 🌲 ",
        "fire": " 🔥 ",
        "hospital": " 🏥 ",
        "shop": " 🛒 ",
        "river": " 💧 ",
        "helicopter": " 🚁 "
    }

    for y in range(len(game_map)):
        row = ""
        for x in range(len(game_map[y])):
            if (x, y) == (heli.x, heli.y):
                row += symbols["helicopter"]
            elif game_map[y][x] == "fire":
                row += symbols["fire"]
            elif game_map[y][x] == "tree":
                row += symbols["tree"]
            elif game_map[y][x] == "river":
                row += symbols["river"]
            elif game_map[y][x] == "hospital":
                row += symbols["hospital"]
            elif game_map[y][x] == "shop":
                row += symbols["shop"]
            else:
                row += symbols["empty"]
        print(row)

def main():
    print("Добро пожаловать в игру 'Пожарный вертолёт'!")
    choice = input("Начать новую игру (n) или загрузить сохранение (l)? ").lower()
    if choice == "l":
        heli, fire_manager, game_map = load_game()
    else:
        width = int(input("Введите ширину поля: "))
        height = int(input("Введите высоту поля: "))
        tree_count = int(input("Сколько деревьев разместить? "))
        river_count = int(input("Сколько рек создать? "))
        hospital_count = int(input("Сколько госпиталей добавить? "))
        shop_count = int(input("Сколько магазинов добавить? "))

        generator = MapGenerator(width, height)
        game_map = generator.generate_trees(tree_count)
        game_map = generator.generate_rivers(river_count)
        game_map = generator.generate_special_cells(hospital_count, "hospital")
        game_map = generator.generate_special_cells(shop_count, "shop")

        heli = Helicopter(0, 0, game_map)
        fire_manager = FireManager(game_map)

    try:
        while True:
            print("\n" + "-" * 50)
            print(f"Очки: {heli.points} | Жизни: {heli.lives} | Вода: {heli.water}/{heli.tank_capacity}")
            print_map(game_map, heli)
            print("Управление: W/A/S/D - движение, F - потушить, E - улучшения, Q - выход")

            move = input("Ваш ход: ").lower()

            if move == "w":
                heli.move(-1, 0)
            elif move == "s":
                heli.move(1, 0)
            elif move == "a":
                heli.move(0, -1)
            elif move == "d":
                heli.move(0, 1)
            elif move == "f":
                heli.extinguish_fire(fire_manager)
            elif move == "e":
                heli.visit_shop()
            elif move == "q":
                save_choice = input("Сохранить игру перед выходом? (y/n): ").lower()
                if save_choice == "y":
                    save_game(heli, fire_manager, game_map)
                break
            else:
                print("Неизвестная команда.")

            fire_manager.update_fires(game_map, heli)
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nИгра прервана пользователем.")
        save_choice = input("Сохранить игру перед выходом? (y/n): ").lower()
        if save_choice == "y":
            save_game(heli, fire_manager, game_map)

if __name__ == "__main__":
    main()