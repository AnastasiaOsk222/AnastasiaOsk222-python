def count_divisors(x):
    # Возвращает количество делителей числа x
    count = 0
    sqrt_x = int(x ** 0.5)
    
    for i in range(1, sqrt_x + 1):
        if x % i == 0:
            count += 1
            if i != x // i:
                count += 1
    return count

while True:
    try:
        X = int(input("Введите натуральное число ≥ 1: "))
        if X < 1:
            raise ValueError("Число должно быть больше или равно 1")
        if X > 2e9:
            raise ValueError("Число не должно превышать 2 миллиарда (2e9)")
        break
    except ValueError as e:
        print(f"Ошибка ввода: {e}. Попробуйте ещё раз.")

result = count_divisors(X)
print(f"Количество натуральных делителей числа {X}: {result}")