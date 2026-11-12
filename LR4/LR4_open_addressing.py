import math

# Константа розміру таблиці
M = 13
M2 = 16
# Список вхідних слів
WORDS = ["НЕ", "КЛАДИ", "ВСІ", "ЯЙЦЯ", "В", "ОДИН", "КОШИК", "ЩОБ", "НЕ", "ВТРАТИТИ", "ВСЕ", "ОДРАЗУ"]
# Словник позицій
LETTER_POSITIONS = {
    'А': 1,  'Б': 2,  'В': 3,  'Г': 4,  'Ґ': 5,  'Д': 6,  'Е': 7,
    'Є': 8,  'Ж': 9,  'З': 10, 'И': 11, 'І': 12, 'Ї': 13, 'Й': 14,
    'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19, 'П': 20, 'Р': 21,
    'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}

def primary_hash(key: str) -> int:
    """h(k) = (сума позицій букв) mod M. Первинна хеш-функція."""
    sum_of_positions = 0
    for char in key:
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position
    return sum_of_positions % M

def hash_2(key: str) -> int:
    """h(k) = (сума позицій букв) mod M. Первинна хеш-функція."""
    sum_of_positions = 0
    for char in key:
        position = LETTER_POSITIONS.get(char, 0)
        sum_of_positions += position

    res = (sum_of_positions * 0.6180339887) % 1
    return math.floor(M2 * res)
    
def build_closed_hash_table(words: list, m: int, f) -> list:
    """
    Будує хеш-таблицю з відкритою адресацією, використовуючи лінійне дослідження.
    """
    # 1. Ініціалізація таблиці: M порожніх слотів (використовуємо None як "порожній")
    hash_table = [None] * m
    inserted_count = 0
    # 2. Обробка кожного слова
    for word in words:
        # Крок 2a: Обчислення початкової адреси
        start_address = f(word)
        address = start_address

        # Крок 2b: Лінійне дослідження (Linear Probing)
        # Цикл гарантує, що ми не будемо шукати нескінченно довго у повній таблиці
        for i in range(m):
            # h(k, i) = (h(k) + i) mod M
            address = (start_address + i) % m
            # Перевірка, чи комірка вільна
            if hash_table[address] is None:
                # Вставлення ключа
                hash_table[address] = word
                inserted_count += 1
                break
            # Якщо комірка зайнята, продовжуємо цикл (наступна ітерація i збільшить крок на 1)
        else:
            # Цей блок виконується, якщо цикл завершився без 'break' (таблиця повна)
            print(f"Помилка: Таблиця заповнена. Не вдалося додати слово: {word}")
    return hash_table
    
def display_hash_table(table: list, m: int):
    """Виводить хеш-таблицю у зручному форматі."""
    print(f"\n--- Хеш-таблиця (Відкрита адресація, M={m}) ---")
    print("Індекс | Слово")
    print("-------|-------")
    for i, item in enumerate(table):
    # Виводимо ключі або позначку, що комірка порожня
        value = item if item is not None else "(NULL)"
        print(f"{i:02d} | {value}")

# Виконання:
hash_table = build_closed_hash_table(WORDS, M, primary_hash)
hash_table_2 = build_closed_hash_table(WORDS, M2, hash_2)
display_hash_table(hash_table, M)
display_hash_table(hash_table_2, M2)