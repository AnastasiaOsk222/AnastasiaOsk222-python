pets = {}

# Имя питомца
pet_name = input("Введите имя питомца: ")

# Вид питомца
pet_type = input("Введите вид питомца: ")

# Возраст питомца и проверяем, что это целое число
while True:
    try:
        pet_age = int(input("Введите возраст питомца: "))
        if pet_age <= 0:
            print("Возраст должен быть положительным числом.")
            continue
        break
    except ValueError:
        print("Пожалуйста, введите корректный возраст (целое число).")

# Имя владельца
owner_name = input("Введите имя владельца: ")

# Формируем внутренний словарь с информацией о питомце
pet_info = {
    "Вид питомца": pet_type,
    "Возраст питомца": pet_age,
    "Имя владельца": owner_name
}

# Добавляем информацию о питомце во внешний словарь
pets[pet_name] = pet_info

# Определяем правильное окончание для слова "год"
def get_year_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif age % 10 in [2, 3, 4]:
        return "года"
    else:
        return "лет"

# Получаем информацию из словаря
for name in pets.keys():
    info = pets[name]
    pet_type = info["Вид питомца"]
    pet_age = info["Возраст питомца"]
    owner_name = info["Имя владельца"]

    # Строка с возрастом и правильным окончанием
    age_suffix = get_year_suffix(pet_age)
    age_str = f"{pet_age} {age_suffix}"

    # Результат. Строка с информацией
    result_string = f'Это {pet_type} по кличке "{name}". Возраст питомца: {age_str}. Имя владельца: {owner_name}.'
    print(result_string)