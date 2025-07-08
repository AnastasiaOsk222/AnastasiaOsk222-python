my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list_recursive(index=0):
    # Рекурсивная функция для вывода элементов списка.
    if index >= len(my_list):
        print("Конец списка")
        return
    print(my_list[index])
    print_list_recursive(index + 1)  # Рекурсивный вызов для следующего элемента

# Запуск рекурсивной функции
print_list_recursive()