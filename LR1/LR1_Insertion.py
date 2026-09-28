def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # Цикл ітерується від другого елемента до кінця
    # i - це індекс елемента, який потрібно вставити
    for i in range(1, n):
        print("------------------------------")
        print(f"Ітерація {i}:")
        # Зберігаємо поточний елемент для вставки
        key = arr[i]
        assignments += 1
        print("  Елемент для вставки (key):", key)
        print("  Відсортована частина:", arr[:i])
        # j - індекс попереднього елемента
        j = i - 1
        assignments += 1

        # Пересуваємо елементи, що більші за key,
        # вправо, щоб звільнити місце для вставки
        while j >= 0 and arr[j] > key:
            print(f"  Порівняння: {arr[j]} > {key}. True. Зсуваємо {arr[j]} вправо.")
            comparisons += 1 # Порівняння в умові while
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1
        if j < 0:
            print("  Досягнуто початку масиву. Цикл завершено.")
        else: print(f"  Порівняння: {arr[j]} > {key}. False. Цикл завершено.")
        
        # Додаткове порівняння, коли умова while стає false
        # (якщо j не стало менше 0)
        if j >= 0:
            comparisons += 1

        print(f"  Вставка {key} на позицію {j + 1}.")
        # Вставляємо key на його правильне місце
        arr[j + 1] = key
        assignments += 1

        print(f"  Масив після ітерації {i}:", arr)

    print("------------------------------")
    return arr, comparisons, assignments

# Приклад використання
my_list = [38, 15, 50, 99, 41, 52, 47, 65, 95]  # Варіант 1
print("Оригінальний список:", my_list)

sorted_list, comps, assigs = insertion_sort(my_list.copy())
# Використання .copy(), щоб не змінювати оригінал
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")