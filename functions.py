def sum_digits(number):
    """Возвращает сумму цифр модуля числа."""
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


def average(numbers):
    """Возвращает среднее или None для пустого списка."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


def normalize_text(text):
    """Нижний регистр, без пробелов по краям, один пробел между словами."""
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    """Вариант 1: возвращает числа больше порога (порядок и повторы сохраняются)."""
    result = []
    for num in numbers:
        if num > threshold:
            result.append(num)
    return result


def is_palindrome(text):
    """Дополнительно: палиндром по правилам работы №5. Пустой — False."""
    cleaned = text.lower().replace(" ", "")
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]
