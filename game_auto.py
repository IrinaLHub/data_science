
"""Игра угадай число"""

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    # Используем метод деления отрезка пополам
    count = 0
    min_range = 1    # нижняя граница диапазона поиска
    max_range = 100  # верхняя граница диапазона поиска
    predict = 50     # предсказанное число, начальное значение - середнее

    while number != predict:
        count += 1        
        if number > predict:
            min_range = predict
        elif number < predict:
            max_range = predict
        predict = min_range + ((max_range-min_range+1) // 2)

    # Ваш код заканчивается здесь

    return count
