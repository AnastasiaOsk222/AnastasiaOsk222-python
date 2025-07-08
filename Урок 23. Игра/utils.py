import pickle

def save_game(heli, fire_manager, game_map):
    with open("savegame.pkl", "wb") as f:
        pickle.dump((heli, fire_manager, game_map), f)
    print("Игра сохранена!")

def load_game():
    try:
        with open("savegame.pkl", "rb") as f:
            heli, fire_manager, game_map = pickle.load(f)
        print("Игра загружена!")
        return heli, fire_manager, game_map
    except FileNotFoundError:
        print("Сохраненных игр не найдено.")
        exit()