import numpy as np
import random

# Функция для генерации массива случайных чисел
def generate_random_array(seed, length):
    np.random.seed(seed)
    return np.random.randint(1, 201, size=length).tolist()

# Функция для поиска сида по заданному массиву
def find_seed(target_array, attempts=1000):
    length = len(target_array)
    checked_seeds = set()  # Храним проверенные сиды, чтобы избежать повторений
    
    for _ in range(attempts):  # Цикл по количеству попыток
        seed = random.randint(0, 2**32 - 1)  # Генерируем случайный сид
        if seed in checked_seeds:
            continue  # Если сид уже был проверен, пробуем другой
        
        checked_seeds.add(seed)
        generated_array = generate_random_array(seed, length)
        
        # Вывод информации о текущем сидe и результате сравнения
        if generated_array == target_array:
            print(f"{seed} 1 {generated_array}")  # Сид соответствует
            return seed
        else:
            print(f"{seed} 0 {generated_array}")  # Сид не соответствует
    
    return None  # Если сид не найден после всех попыток

# Пример использования
target_array = [10, 20, 30, 40, 50]  # Замените на ваш массив

# Поиск сида для заданного массива
found_seed = find_seed(target_array)
if found_seed is not None:
    print(f"Найден сид: {found_seed}")
else:
    print("Сид не найден.")
