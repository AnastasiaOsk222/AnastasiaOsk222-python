# Ввод последовательности чисел
numbers = list(map(int, input("Введите числа через пробел: ").split()))

# Множество для хранения уже встреченных чисел
seen = set()

# Обработка каждого числа
for num in numbers:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)