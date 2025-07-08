def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_list(start_num):
    # Создаёт список факториалов от start_num до 1 в убывающем порядке.
    return [factorial(i) for i in range(start_num, 0, -1)]

# Ввод натурального числа
try:
    number = int(input("Введите натуральное число: "))
    if number < 1:
        raise ValueError("Число должно быть больше 0.")
    
    # Вычисляем факториал
    fact = factorial(number)
    print(f"Факториал числа {number} равен: {fact}")
    
    # Создаем список факториалов от 'fact' до 1
    result_list = factorial_list(fact)
    print("Список факториалов:", result_list)

except ValueError as e:
    print("Ошибка ввода:", e)