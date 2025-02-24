import numpy as np

# Функция для генерации массива случайных чисел
def generate_random_array(seed, length):
    np.random.seed(seed)
    return np.random.randint(1, 201, size=length).tolist()

# Функция для поиска сида по заданному массиву
def find_seed(target_array):
    length = len(target_array)
    for seed in range(2**32):  # Перебор всех возможных сидов
        generated_array = generate_random_array(seed, length)
        # Вывод информации о текущем сидe и результате сравнения
        if generated_array == target_array:
            print(f"{seed} 1 {generated_array}")  # Сид соответствует
            return seed
        else:
            print(f"{seed} 0 {generated_array}")  # Сид не соответствует
    return None  # Если сид не найден

# Пример использования
target_array = [10, 20, 30, 40, 50]  # Замените на ваш массив

# Поиск сида для заданного массива
found_seed = find_seed(target_array)
if found_seed is not None:
    print(f"Найден сид: {found_seed}")
else:
    print("Сид не найден.")

