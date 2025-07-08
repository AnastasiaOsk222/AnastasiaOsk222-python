m = int(input("Введите максимальную грузоподъемность лодки: "))
n = int(input("Введите количество рыбаков: "))

weights = []
print(f"Введите вес {n} рыбаков (по одному числу на строке):")
for _ in range(n):
    weight = int(input())
    weights.append(weight)

# Сортируем вес
weights.sort()

# Инициализируем два указателя и счетчик лодок
left = 0
right = n - 1
boats = 0

while left <= right:
    if weights[left] + weights[right] <= m:
        # Вместе умещаются рыбаки, сажаем обоих
        left += 1
        boats += 1
    else:
        # Тяжелый едет один
        boats += 1
    right -= 1

# Вывод результата
print("Минимальное количество лодок:", boats)