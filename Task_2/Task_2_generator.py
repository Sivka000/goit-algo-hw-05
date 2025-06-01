import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    numbers = re.findall(r'\b\d+\.?\d*\b', text) #Використання регулярного виразу для знаходження дійсних чисел
    for number in numbers:
        yield float(number) #Повертає число як дійсне

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    total = sum(func(text)) #Підсумовує всі числа отримані з генератора
    return total

with open('Text.txt', 'r', encoding='utf-8') as file: #Отримує дані з текстового файлу
    text = file.read()

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
