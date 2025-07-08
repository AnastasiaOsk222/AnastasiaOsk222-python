N = int(input("Введите число N: "))

# Проверка на корректность
if N < 1 or N > 10000:
    print("Некорректное значение N")
else:
    # Считываем N чисел
    numbers = [int(input()) for _ in range(N)]

    # Переворачиваем список
    reversed_numbers = numbers[::-1]

    # Выводим перевёрнутый список
    for num in reversed_numbers:
        print(num)