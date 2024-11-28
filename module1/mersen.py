from math import sqrt


def mersen(n):
    simple_numbers = [2]
    numbers = []

    for i in range(3, n + 1, 2):
        if i > 10 and i % 10 == 5:
            continue
        for j in simple_numbers:
            if j > int((sqrt(i)) + 1):
                simple_numbers.append(i)
                break
            if i % j == 0:
                break
        else:
            simple_numbers.append(i)

    for i in simple_numbers:
        numbers.append(2 ** i - 1)

    return numbers[-1]