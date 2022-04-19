import math


def main(y, z, x):
    first = math.sqrt(70 * (y ** 5) - (56 * z - 23 * (x ** 3)) ** 7)
    second = 27 * (z ** 2) + (x ** 2 - y ** 3 - y) ** 6
    third = 60 * ((62 * y - z ** 2 - y ** 3) ** 3)
    third_lol = math.tan(1 - 79 * (z ** 2) - 26 * x) ** 6
    some = first + (second / (third - third_lol))
    return some


main(0.09, -0.63, -0.18)
main(0.04, -0.82, 0.66)

import math


def main(n, b, m):
    sum = 0
    for i in range(1, m + 1):
        for j in range(1, b + 1):
            for k in range(1, n + 1):
                lol = math.atan((i ** 3) / 49 - 46 * (j ** 2) - 2 * i) ** 3
                sum += lol - k
    return sum


main(6, 6, -0.1)
main(4, 7, -0.37)



import math


def main(y, x, z):
    first = 77 * (91 * (x ** 3) - x - 25 * (x ** 2)) ** 3
    second = ((84 * (z ** 2) - 1 - 42 * (y ** 3)) ** 7) / 60
    third = 91 * math.acos(81 * y ** 2 - 21 * z ** 3 - x)
    some = math.sqrt(first - second) - third
    return some


main(0.12, 0.78, -0.14)
main(-0.06, 0.67, 0.13)



import math


def main(x):
    if x < 98:
        return (26 + x ** 2 + 23 * x) ** 6 / 78
    elif 98 <= x < 180:
        a = (x ** 3 + 1 + 76 * x) ** 7
        b = 61 * math.floor(51 - x) ** 6
        c = 48 * math.floor(x ** 2 + x + x ** 3 / 37) ** 5
        result = a + b + c
        return result
    elif 180 <= x < 257:
        return 46 * x ** 7
    elif 257 <= x < 313:
        return 11 * (19 * x ** 3 + x ** 2) ** 3
    elif x >= 313:
        return (x - x ** 3 / 19) ** 6


main(294)
main(148)



def f(x, y, z):
    n = len(x)
    sum = 0
    for i in range(0, n):
        sum += (96*y[math.ceil(i/3)]**3 - 58*z[n-i+2] - 87*x[n-i+2]**2)**6
    return sum

f([-0.4, -0.23, 0.35, -0.35],
[0.16, -0.68, -0.44, -0.53],
[-0.64, -0.82, -0.06, -0.9]), f([0.27, 0.35, -0.04, -0.14],
[0.14, 0.72, -0.38, 0.46],
[0.73, -0.19, -0.82, -0.18])