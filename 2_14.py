from tabulate import tabulate

table = [["Sun", 696000, 1989100000], ["Earth", 6371, 5973.6],
         ["Moon", 1737, 73.5], ["Mars", 3390, 641.85]]
# print(tabulate(table))
# print()
# print(tabulate(table, headers='firstrow'))
# print()
# print(tabulate(table, headers='keys'))
# print()
# print(tabulate(table, showindex="always"))


def your_choise(table):
    print('Список доступных тегов для tablefmt: textile, youtrack, moinmoin, mediawiki, rst\n'
          'jira, orgtbl, pipe, psql, pretty, presto, fancy_grid, grid, github, simple')
    tablefmt_tag = input('Выберите тег для tablefmt: ')
    print('Список доступных тегов для headers: firstrow, keys')
    headers_tag = input('Выберите тег для headers: ')
    return tabulate(table, headers=headers_tag, tablefmt=tablefmt_tag)


# print(tabulate(table, tablefmt="simple"))
# print()
# print(tabulate(table, tablefmt="github"))
# print()
# print(tabulate(table, tablefmt="grid"))
# print()
# print(tabulate(table, tablefmt="fancy_grid"))
# print()
print(your_choise(table))