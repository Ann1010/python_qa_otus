"""Homework 1."""


def calculate_average(numbers: list[int]) -> float:
    """
    Нахождение среднего значения.

    :param numbers: список элементов
    :return:
    """
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
