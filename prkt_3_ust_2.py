from memory_profiler import memory_usage
from types import FunctionType

print(memory_usage())
print(dir())
print(dir())
print(memory_usage())
import matplotlib

print(memory_usage())
matplotlib.__all__ = ['MutableMapping']

from matplotlib import *

print(memory_usage())
print(memory_usage())
print(dir())


class exp:
    def __init__(self):
        self.two = 6
        self.one = 7
        self.three = 8
        print('bdaa')
# print(math.floor(1.234))
print(dir())
limpia = exp()
print(vars(limpia))
name_1 = 'two'
name_2 = 'one'
print(getattr(limpia, name_1))
print(getattr(limpia, name_2))
class Foo:
    def bar(self): print(1)
    def baz(self): print(2)
    def init_bar(self):
        s = Foo()
        s.bar()

def methods(cls):
    return [x for x, y in cls.__dict__.items() if type(y) == FunctionType]

print(methods(Foo))  # ['bar', 'baz']
some_per = Foo()
# some_per.baz()



