"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0  # количество попыток
    min_number = 0  # минимальное значение поиска
    max_number = 101  # максимальное значение поиска
    mid_number = 50  # cреднее значение поиска
    
    while True:# реализуем бинарный поиск 
        count += 1
        if mid_number == number:
            return count # выход из цикла если угадали число
        
        if mid_number > number:
            max_number = mid_number # перезаписываем максимальное значение поиска
        elif mid_number < number:
            min_number = mid_number # перезаписываем минимальное значение поиска
        mid_number = (min_number + max_number)//2
   
          


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
