import math

def f(x, y, z):
    n = len(x) # 4
    sum_x = 0
    sum_y = 0
    sum_z = 0
    summa = 0
    for i in range(1, len(x) + 1): # jn 0 lj 3
        print(math.ceil(n + 1 - (i + 1) / 3), n + 1 - i - 1)
        sum_y = 96 * (y[math.ceil((i - 1) / 3)] ** 3)
        sum_z = 58 * z[n - i]
        sum_x = 87 * (x[n - i] ** 2)
        summa += (sum_y - sum_z - sum_x) ** 6
    return summa


print(f([-0.4, -0.23, 0.35, -0.35],
[0.16, -0.68, -0.44, -0.53],
[-0.64, -0.82, -0.06, -0.9]), f([0.27, 0.35, -0.04, -0.14],
[0.14, 0.72, -0.38, 0.46],
[0.73, -0.19, -0.82, -0.18]))

MAMA_PAPA = 90