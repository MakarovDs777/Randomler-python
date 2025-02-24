import numpy as np
import random

# Функция для генерации массива случайных чисел
def generate_random_array(seed, length):
    np.random.seed(seed)
    return np.random.randint(1, 201, size=length).tolist()

# Функция для поиска сида по заданному массиву
def find_seed(target_array):
    length = len(target_array)
    checked_seeds = set()  # Храним проверенные сиды

    while True:  # Бесконечный цикл до нахождения сида
        seed = random.randint(0, 2**32 - 1)  # Генерируем случайный сид
        if seed in checked_seeds:
            continue  # Пропускаем, если сид уже был проверен
        
        checked_seeds.add(seed)  # Запоминаем проверенный сид
        generated_array = generate_random_array(seed, length)
        
        # Вывод информации о текущем сидe и результате сравнения
        if generated_array == target_array:
            print(f"{seed} 1 {generated_array}")  # Сид соответствует
            return seed
        else:
            print(f"{seed} 0 {generated_array}")  # Сид не соответствует

# Пример использования
target_array = [10, 20, 30, 40, 50]  # Замените на ваш массив

# Поиск сида для заданного массива
found_seed = find_seed(target_array)
print(f"Найден сид: {found_seed}")

