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
            return count
        
        if mid_number > number:
            max_number = mid_number # перезаписываем максимальное значение поиска
        elif mid_number < number:
            min_number = mid_number # перезаписываем минимальное значение поиска
        mid_number = (min_number + max_number)//2
   
          # выход из цикла если угадали число
          
