import doctest


def bucketsort(n):
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:  # перехватываем значения типа 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


def lolkek():
    print(4)


if __name__ == "__main__":
    # doctest.testfile('test.txt')
    doctest.testfile("test.txt")
    # doctest.testmod()
