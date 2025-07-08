word = input("Введите слово из латинских букв: ").lower()

# Множество гласных
vowels = {'a', 'e', 'i', 'o', 'u'}

# Счетчик для подсчёта гласных
vowel_count = {v: 0 for v in vowels}

# Подсчёт гласных
for char in word:
    if char in vowels:
        vowel_count[char] += 1

# Общее количество гласных и согласных
total_vowels = sum(vowel_count.values())
total_consonants = len(word) - total_vowels

# Вывод результатов
print(f"Количество гласных: {total_vowels}")
print(f"Количество согласных: {total_consonants}")

# Вывод количества каждой гласной или False, если её нет
for v in vowels:
    count = vowel_count[v]
    if count == 0:
        print(f"{v}: False")
    else:
        print(f"{v}: {count}")