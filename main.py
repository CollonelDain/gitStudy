from module1.fibonachi import recursiveFib, iterativeFib, formulaBineFib
from module1.mersen import mersen


if __name__ == '__main__':
    number = input("Введите n-ое число Фибоначчи: ")

    try:
        if not number.isdigit():
            raise TypeError
        number1 = int(number)
        print("Результат рекурсивной функции: ", recursiveFib(number1))
    except TypeError as e:
        print("Введите число!")
    except Exception as e:
        print(f"Не удалось вычислить рекурсивно\nОшибка: {e}")

    try:
        print("Результат интерактивной функции: ", iterativeFib(number))
    except TypeError as e:
        print("Введите число!")
    except Exception as e:
        print(f"Не удалось вычислить интерактивно\nОшибка: {e}")

    try:
        print("Результат функции Бине: ", formulaBineFib(number))
    except TypeError as e:
        print("Введите число!")
    except Exception as e:
        print(f"Не удалось вычислить по формуле Бине\nОшибка: {e}")

    n = int(input("Введите порядковый номер числа Мерсена: "))
    print(f'{n} число Мерсена: {mersen(n)}')