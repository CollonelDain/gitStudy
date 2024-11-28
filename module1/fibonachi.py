import decimal


def recursiveFib(n):
    if n == 1 or n == 2:
        return 1

    return recursiveFib(n - 1) + recursiveFib(n - 2)


def iterativeFib(n):
    if not n.isdigit():
        raise TypeError
    n = int(n)

    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b

    return a


def formulaBineFib(n):
    if not n.isdigit():
        raise TypeError
    n = int(n)

    decimal.getcontext().prec = 10000

    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)

    a = ((phi ** n) - ((-phi) ** -n)) / root_5

    return round(a)