A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B (не меньше A): "))

even_numbers = []

# Перебираем все числа от A до B включительно
for num in range(A, B + 1):
    if num % 2 == 0:
        even_numbers.append(str(num))

# Вывод результата через пробел
print(" ".join(even_numbers))