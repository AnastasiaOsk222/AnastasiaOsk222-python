N = int(input("Введите число N: "))

# Проверка на корректность ввода
if N < 0:
    print("Ошибка: количество чисел не может быть отрицательным.")
else:
    count_zero = 0

    # Ввод ровно N целых чисел
    print(f"Введите {N} целых чисел:")
    for _ in range(N):
        num = int(input())
        if num == 0:
            count_zero += 1

    # Вывод результата
    print(f"Количество нулей: {count_zero}")