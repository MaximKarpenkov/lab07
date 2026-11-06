from functions import sum_digits, average, normalize_text, select_numbers

def main():
    # 1. Целое число для sum_digits
    number = int(input("Введите целое число: "))
    print(f"Сумма цифр: {sum_digits(number)}")

    # 2. Список чисел для average и select_numbers
    raw_numbers = input("Введите числа через пробел: ")
    numbers = []
    if raw_numbers.strip():
        for part in raw_numbers.split():
            numbers.append(int(part))

    avg = average(numbers)
    if avg is None:
        print("Среднее: Нет данных")
    else:
        print(f"Среднее: {avg:.2f}")

    # 3. Порог и выборка (вариант 1)
    threshold = int(input("Введите порог: "))
    selected = select_numbers(numbers, threshold)
    print(f"Числа больше {threshold}: {selected}")

    # 4. Произвольный текст для normalize_text
    text = input("Введите текст: ")
    print(f"Нормализовано: {normalize_text(text)!r}")


if __name__ == "__main__":
    main()
