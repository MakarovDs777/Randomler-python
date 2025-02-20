import numpy as np

# Функция для генерации массива случайных чисел
def generate_random_array(seed, length):
    np.random.seed(seed)
    return np.random.randint(1, 201, size=length).tolist()

# Пример использования
seed = 333638342
length = 241

# Генерация массива
generated_array = generate_random_array(seed, length)
print("Сгенерированный массив:", generated_array)

# Используем изначальный сид и длину массива
computed_seed = seed
computed_length = length

# Восстановление массива
retrieved_array = generate_random_array(computed_seed, computed_length)
print("Восстановленный массив:", retrieved_array)

# Проверка на совпадение
if generated_array == retrieved_array:
    print("Сгенерированный массив совпадает с восстановленным!")
else:
    print("Сгенерированный массив не совпадает с восстановленным!")
