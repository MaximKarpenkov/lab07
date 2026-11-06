from functions import (
    average,
    normalize_text,
    sum_digits,
    select_numbers,
    is_palindrome,
)

# Базовые проверки из задания
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# Проверки варианта 1: select_numbers (больше порога)
assert select_numbers([-5, 0, 2, 5], 2) == [5]
assert select_numbers([], 2) == []
assert select_numbers([3, 3, 4], 2) == [3, 3, 4]   # повторы сохраняются
assert select_numbers([2, 2, 2], 2) == []           # граница: строго больше
assert select_numbers([3], 2) == [3]
assert select_numbers([-1, 0, 1], 0) == [1]

# Исходный список не изменяется
original = [-5, 0, 2, 5]
saved_copy = original.copy()
select_numbers(original, 2)
assert original == saved_copy

# Дополнительно: палиндром
assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("Python") is False
assert is_palindrome("   ") is False

print("Все проверки пройдены")
