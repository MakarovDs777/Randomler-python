import numpy as np

# Функция для генерации массива случайных чисел
def generate_random_array(seed, length):
    np.random.seed(seed)
    return np.random.randint(1, 201, size=length).tolist()

# Функция для получения сида и длины массива
def compute_seed_and_length(random_array):
    length = len(random_array)
    seed = hash(tuple(random_array)) % (2**32)  # Это не будет работать надежно!
    return seed, length

# Пример использования
seed = 333638342
length = 241

# Генерация массива
generated_array = generate_random_array(seed, length)
print("Сгенерированный массив:", generated_array)

# Получение сида и длины
computed_seed, computed_length = compute_seed_and_length(generated_array)
print("Сид:", computed_seed)
print("Длина массива:", computed_length)

# Восстановление массива
retrieved_array = generate_random_array(computed_seed, computed_length)
print("Восстановленный массив:", retrieved_array)

# Проверка на совпадение
if generated_array == retrieved_array:
    print("Сгенерированный массив совпадает с восстановленным!")
else:
    print("Сгенерированный массив не совпадает с восстановленным!")
