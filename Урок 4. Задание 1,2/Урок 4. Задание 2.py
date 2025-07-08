number = int(input("Введите пятизначное число: "))

# Проверка, что число пятизначное
if 10000 <= number <= 99999:
    # Разряды числа
    units = number % 10 # Единицы
    tens = (number // 10) % 10 # Десятки
    hundreds = (number // 100) % 10 # Сотни
    thousands = (number // 1000) % 10 # Тысячи
    ten_thousands = (number // 10000) # Десятки тысяч

    try:
        result = (tens ** units) * hundreds / (ten_thousands - thousands)
        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль (разность десятков тысяч и тысяч равна нулю).")
else:
    print("Ошибка: Введите корректное пятизначное число.")