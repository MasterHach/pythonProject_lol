from sympy import *


def deriv(func):
    x = Symbol('x')
    y = x ** 3
    derivative_y = y.diff(x)
    new_f = lambdify(x, derivative_y)
    return lambda res: func(new_f(res))


print(deriv(lambda x: x)(5))
