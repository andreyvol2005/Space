# Проект «Space»: простая программа на языке Python
# Ветвь: ВтораяВетвь (лабораторная работа №5 по информатике)


def factorial(n: int) -> int:
    """Вычисляет факториал числа n (n! = 1 * 2 * ... * n)."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main() -> None:
    """Выводит факториалы чисел от 1 до 10."""
    for n in range(1, 11):
        print(f"{n}! = {factorial(n)}")


if __name__ == "__main__":
    main()
