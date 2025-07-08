number = int(input("Введите целое число: "))

if number == 0:
    print("нулевое число")
else:
    sign = "отрицательное" if number < 0 else "положительное"
    parity = "четное" if number % 2 == 0 else "нечетное"
    
    if number % 2 == 0:
        print(f"{sign} {parity} число")
    else:
        print("число не является четным")