def merge_sort_recursive(arr, indents=1):
    comparisons = 0
    assignments = 0
    recursive_calls = 0
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
    mid = len(arr) // 2
    assignments += 1
    # Підрахунок рекурсивних викликів
    recursive_calls += 2
    # Рекурсивно ділимо масив на дві половини
    # Рекурсивно ділимо масив на дві половини
    print("  " * indents + "Розділяємо масив:", arr[:mid])
    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid], indents+1)
    print("  " * indents + "Розділяємо масив:", arr[mid:])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:], indents+1)
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
    # Зливаємо відсортовані половини
    merged_arr, c_merge, a_merge = merge(left_half, right_half, indents)
    print("  " * (indents-1) + "Злиття завершено. Результат:", merged_arr)
    comparisons += c_merge
    assignments += a_merge
    return merged_arr, comparisons, assignments, recursive_calls
    
def merge(left, right, indents=0):
    print("  " * indents + "Зливаємо", left, "та", right)
    merged_arr = []
    comparisons = 0
    assignments = 0
    i = 0
    j = 0
    # Зливаємо елементи з обох масивів
    while i < len(left) and j < len(right):
        print("  " * (indents+1) + "Порівняння:", left[i], "<=", right[j], "->", left[i] <= right[j], end='. Додаємо ')
        comparisons += 1
        if left[i] <= right[j]:
            print(left[i])
            merged_arr.append(left[i])
            i += 1
        else:
            print(right[j])
            merged_arr.append(right[j])
            j += 1
        assignments += 1

    # Додаємо елементи, що залишилися
    while i < len(left):
        print("  " * (indents+1) + "Додаємо залишок з лівого масиву: ", left[i])
        merged_arr.append(left[i])
        i += 1
        assignments += 1

    while j < len(right):
        print("  " * (indents+1) + "Додаємо залишок з правого масиву: ", right[j])
        merged_arr.append(right[j])
        j += 1
        assignments += 1
    return merged_arr, comparisons, assignments

# Приклад використання
my_list = [10, 90, 95, 30, 45, 60, 57, 28, 5]  # Варіант 14
print("--- РЕКУРСИВНА ВЕРСІЯ ---")
print("Розділяємо масив:", my_list)
sorted_list, total_comparisons, total_assignments, total_recursive_calls = merge_sort_recursive(my_list)
print("Відсортований список:", sorted_list)
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")