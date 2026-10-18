def swap(arr, i, j):
    """Міняє місцями два елементи в масиві."""
    arr[i], arr[j] = arr[j], arr[i]

def sink(arr, i, n):
    """
    Процедура 'занурення' елемента вниз по купі.
    A: масив
    i: індекс поточного елемента
    n: розмір купи
    """
    assignments, comparisons = 0, 0
        
    k = i
    assignments += 1
    while True:
        j = 2 * k + 1 # Індекс лівого дочірнього елемента
        assignments += 1

        comparisons += 1
        if j >= n:
            break

        # Знаходимо індекс найбільшого дочірнього елемента
        comparisons += 2
        if j + 1 < n and arr[j + 1] > arr[j]:
            assignments += 1
            j += 1

        # Якщо поточний елемент більший або дорівнює найбільшому дочірньому
        comparisons += 1
        if arr[k] >= arr[j]:
            break

        # Міняємо місцями та продовжуємо занурення
        swap(arr, k, j)
        assignments += 2

        k = j
        assignments += 1 
    return assignments, comparisons

def heapsort(arr):
    """
    Алгоритм пірамідального сортування.
    """
    assignments, comparisons = 0, 0

    n = len(arr)
    assignments += 1

    print(f"Початковий масив: {arr}\n")

    # Фаза 1: Побудова максимальної купи
    # Починаємо з першого елемента, що має дочірні елементи.
    print("--- Фаза 1: Побудова максимальної купи ---")
    for i in range(n // 2 - 1, -1, -1):
        comparisons += 1 # Перевірка умови циклу
        print(f"Занурюємо елемент з індексу {i}: {arr[i]}")
        a, c = sink(arr, i, n)
        assignments += a
        comparisons += c
    comparisons += 1 # Умова виходу з циклу
    print(f"\nМасив після побудови купи: {arr}\n")

    # Фаза 2: Сортування
    print("--- Фаза 2: Сортування ---")
    for i in range(n - 1, 0, -1):
        comparisons += 1 # Перевірка умови циклу
        # Переносимо найбільший елемент (корінь) в кінець
        print(f"Міняємо місцями корінь ({arr[0]}) та останній елемент ({arr[i]})")
        swap(arr, 0, i)
        assignments += 2
        # Зменшуємо розмір купи та відновлюємо її властивості
        n -= 1
        assignments += 1
        print(f"Розмір купи зменшився до {n}. Відновлюємо властивості купи.")
        a, c = sink(arr, 0, n)
        assignments += a
        comparisons += c
        print(f"Масив на поточному кроці: {arr}\n")
    comparisons += 1 # Умова виходу з циклу
    return assignments, comparisons, arr

# Моделювання
A = [10, 90, 95, 30, 45, 60, 57, 28, 5]    # Варіант 14
assignments, comparisons, sorted_A = heapsort(A)
print(f"Відсортований масив: {sorted_A}")
print(f"Кількість присвоювань: {assignments}")
print(f"Кількість порівнянь: {comparisons}")
