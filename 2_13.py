from graphviz import Digraph
import os

p = os.path.abspath('main.py')
print(p)
name = input("Введите путь с которого нам начать: ")

way = os.listdir(name)
print(way)
# print(os.path.exists('C:/$Recycle.Bin/S-1-5-18/'))
# print(os.access("C:/$Recycle.Bin/S-1-5-18/", os.W_OK))
# print(os.listdir('C:/$Recycle.Bin/S-1-5-18/'))
dot = Digraph(comment='The Test Table')

wavin = name.split('\\')
print(wavin)


def lolkek(name_g, some):
    for i in os.listdir(name_g):
        #print(i)
        dot.node(i, i)
        dot.edge(some, i, ' ')
        if os.path.isfile(name_g + '\\' + i) or i[0] == '.':
            pass
        else:
            os.chmod(name_g + '\\' + i, 0o700)
            lolkek(name_g + '\\' + i, i)


lolkek(name, wavin[len(wavin) - 1])
dot = Digraph(comment='The Test Table')

# Добавить точку A, метка A - точка A
dot.node('A', 'Dot A')

# Добавить точку B, метка B - точка B
dot.node('B', 'Dot B')
# dot.view()

# Добавить точку C, метка C - точка C
dot.node('C', 'Dot C')
# dot.view()

# Создайте группу ребер, то есть два ребра, соединяющих AB, и одно ребро, соединяющее AC.
dot.edges(['AB', 'AC', 'AB'])
# dot.view()

# Создаем границу между двумя точками
dot.edge('B', 'C', 'test')
# dot.view()


# Получить строковую форму исходного кода DOT
print(dot.source)
# // The Test Table
# digraph {
#   A [label="Dot A"]
#   B [label="Dot B"]
#   C [label="Dot C"]
#   A -> B
#   A -> C
#   A -> B
#   B -> C [label=test]
# }


# Сохранить исходный код в файл и предоставить движок Graphviz
dot.render('test-output/test-table.gv', view=True)