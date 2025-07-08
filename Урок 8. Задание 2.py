N = int(input("Введите число N: "))
arr = list(map(int, input(f"Введите {N} чисел через пробел: ").split()))

# Проверка, что количество чисел совпадает с N
if len(arr) != N:
    print("Ошибка: неверное количество чисел.")
else:
    # Циклический сдвиг вправо
    last_element = arr[-1]
    arr = [last_element] + arr[:-1]

    # Вывод изменённого массива
    print("Изменённый массив:", ' '.join(map(str, arr)))