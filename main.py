from module1.fibonachi import recursiveFib, iterativeFib, formulaBineFib


if __name__ == '__main__':
    number = int(input("Введите n-ое число Фибоначчи: "))

    try:
        print("Результат рекурсивной функции: ", recursiveFib(number))
    except Exception as e:
        print(f"Не удалось вычислить рекурсивно\nОшибка: {e}")

    try:
        print("Результат интерактивной функции: ", iterativeFib(number))
    except Exception as e:
        print(f"Не удалось вычислить интерактивно\nОшибка: {e}")

    try:
        print("Результат функции Бине: ", formulaBineFib(number))
    except Exception as e:
        print(f"Не удалось вычислить по формуле Бине\nОшибка: {e}")
