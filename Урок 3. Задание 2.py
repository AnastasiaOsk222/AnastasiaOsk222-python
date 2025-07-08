# Задание 2. Урок 3

stages = [
    "Australopithecus",
    "Homo habilis",
    "Homo erectus",
    "Homo heidelbergensis",
    "Homo neanderthalensis",
    "Homo sapiens",
    "Homo sapiens sapiens"
]

print("Введите этапы эволюции человека по порядку:")
user_input = []

for i, stage in enumerate(stages):
    answer = input(f"{i+1}-й этап (пример: {stage}): ")
    user_input.append(answer)

print("\nВаш ответ:")
print(*user_input, sep=' => ')