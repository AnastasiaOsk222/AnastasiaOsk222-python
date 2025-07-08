import collections

pets = {}

def get_pet(ID):
    # Возвращает информацию о питомце по его ID или False, если такого нет."""
    return pets[ID] if ID in pets else False

def get_suffix(age):
    # Возвращает правильное окончание для слова 'год' в зависимости от возраста."""
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in [2, 3, 4]:
        return "года"
    else:
        return "лет"

def pets_list():
    # Выводит список всех питомцев из базы данных.
    if not pets:
        print("База данных пуста.")
        return
    for pet_id, pet_info in pets.items():
        name = list(pet_info.keys())[0]
        data = pet_info[name]
        suffix = get_suffix(data["Возраст питомца"])
        print(f"{pet_id}. {name} — {data['Вид питомца']}, возраст: {data['Возраст питомца']} {suffix}, владелец: {data['Имя владельца']}")

# Основные функции CRUD

def create():
    # Добавляет новую запись о питомце.
    global pets
    # Получаем последний ID
    if not pets:
        last_id = 0
    else:
        last_id = collections.deque(pets, maxlen=1)[0]

    new_id = last_id + 1

    name = input("Введите имя питомца: ")
    kind = input("Введите вид питомца: ")

    while True:
        try:
            age = int(input("Введите возраст питомца: "))
            if age <= 0:
                raise ValueError("Возраст должен быть положительным числом.")
            break
        except ValueError as e:
            print(e)

    owner = input("Введите имя владельца: ")

    # Добавляем запись
    pets[new_id] = {
        name: {
            "Вид питомца": kind,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }

    print(f"Питомец '{name}' успешно добавлен с ID {new_id}.")

def read(ID):
    """Выводит информацию о питомце с указанным ID."""
    pet = get_pet(ID)
    if not pet:
        print(f"Питомца с ID {ID} не существует.")
        return

    name = list(pet.keys())[0]
    data = pet[name]
    suffix = get_suffix(data["Возраст питомца"])

    print(f'Это {data["Вид питомца"]} по кличке "{name}". Возраст питомца: {data["Возраст питомца"]} {suffix}. Имя владельца: {data["Имя владельца"]}.')

def update(ID):
    """Обновляет информацию о питомце с указанным ID."""
    pet = get_pet(ID)
    if not pet:
        print(f"Питомца с ID {ID} не существует.")
        return

    name = list(pet.keys())[0]
    data = pet[name]

    print(f"Текущие данные о питомце '{name}':")
    print(f"1. Вид питомца: {data['Вид питомца']}")
    print(f"2. Возраст питомца: {data['Возраст питомца']}")
    print(f"3. Имя владельца: {data['Имя владельца']}")

    field = input("Введите номер поля для изменения (1-3): ")
    if field == "1":
        new_value = input(f"Введите новый вид вместо '{data['Вид питомца']}': ")
        data["Вид питомца"] = new_value
    elif field == "2":
        while True:
            try:
                new_value = int(input(f"Введите новый возраст вместо {data['Возраст питомца']}: "))
                if new_value <= 0:
                    raise ValueError("Возраст должен быть положительным числом.")
                break
            except ValueError as e:
                print(e)
        data["Возраст питомца"] = new_value
    elif field == "3":
        new_value = input(f"Введите новое имя владельца вместо '{data['Имя владельца']}': ")
        data["Имя владельца"] = new_value
    else:
        print("Неверный выбор.")

    print(f"Данные о питомце '{name}' обновлены.")

def delete(ID):
    """Удаляет запись о питомце с указанным ID."""
    if ID in pets:
        del pets[ID]
        print(f"Запись с ID {ID} удалена.")
    else:
        print(f"Питомца с ID {ID} не существует.")

# Основной цикл программы

print("Добро пожаловать в ветеринарную клинику!")

while True:
    command = input("\nВведите команду (create / read / update / delete / list / stop): ").strip().lower()

    if command == "stop":
        print("Работа с базой данных завершена.")
        break

    elif command == "create":
        create()

    elif command == "read":
        try:
            pet_id = int(input("Введите ID питомца для просмотра: "))
            read(pet_id)
        except ValueError:
            print("Неверный формат ID. Должно быть целое число.")

    elif command == "update":
        try:
            pet_id = int(input("Введите ID питомца для обновления: "))
            update(pet_id)
        except ValueError:
            print("Неверный формат ID. Должно быть целое число.")

    elif command == "delete":
        try:
            pet_id = int(input("Введите ID питомца для удаления: "))
            delete(pet_id)
        except ValueError:
            print("Неверный формат ID. Должно быть целое число.")

    elif command == "list":
        pets_list()

    else:
        print("Неизвестная команда. Попробуйте ещё раз.")