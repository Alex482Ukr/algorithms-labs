def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    # Зовнішній цикл ітерується по всьому списку
    # від 0 до n-2 (n-1 проходів)
    for i in range(n - 1):
        print("------------------------------")
        print("Ітерація", i)
        print(f"  Поточний елемент (для обміну): arr[{i}] = {arr[i]}")
        # Припускаємо, що поточний елемент є мінімальним
        min_index = i
        assignments += 1 # Присвоєння змінній min_index

        print("  Шукаємо мінімальний елемент у частині:", arr[i:])
        
        # Внутрішній цикл шукає найменший елемент в решті списку
        for j in range(i + 1, n):
            comparisons += 1 # Операція порівняння
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1 # Присвоєння змінній min_index

        print(f"  Знайдено мінімальний елемент: arr[{min_index}] = {arr[min_index]}")
        # Обмін елементів, якщо знайдено новий мінімальний
        comparisons += 1 # Операція порівняння
        if min_index != i:
            # Обмін елементів
            print(f"  Обмін arr[{i}] ({arr[i]}) і arr[{min_index}] ({arr[min_index]})")
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3 # Три присвоєння при обміні
        print(f"  Масив після ітерації {i}:", arr)
    print("------------------------------")
    return arr, comparisons, assignments

# Приклад використання
my_list = [38, 15, 50, 99, 41, 52, 47, 65, 95]  # Варіант 1
print("Оригінальний список:", my_list)

sorted_list, comps, assigs = selection_sort(my_list.copy())
# Використання .copy(), щоб не змінювати оригінал
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоєнь: {assigs}")