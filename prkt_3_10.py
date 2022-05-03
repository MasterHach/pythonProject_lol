import csv
import datetime
import requests
import matplotlib.pyplot as plt


def kekster(a):
    return a[3]

def kekster_1(a):
    return a[2]


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


def lolik():
    lol_1 = 'https://raw.githubusercontent.com/true-grue/kispython'
    lol_2 = '/main/data/messages.csv'
    response = requests.get(f'{lol_1}{lol_2}').text.splitlines()
    stream = csv.reader(response)
    return list(stream)


def kolik():
    lol_1 = 'https://raw.githubusercontent.com/true-grue/kispython'
    lol_2 = '/main/data/results.csv'
    response = requests.get(f'{lol_1}{lol_2}').text.splitlines()
    stream = csv.reader(response)
    return list(stream)


results = kolik()
message = lolik()
message.sort(key=kekster)
results.sort(key = kekster_1)

mes_groups = sorted(list(set([i[3] for i in message])))
counts = [0] * len(mes_groups)
j = 0
for i in range(len(message)):
    if message[i][3] == mes_groups[j]:
        counts[j] += 1
    else:
        j += 1
        counts[j] += 1
# count = 0
# for i, j in zip(mes_groups, counts):
#     count += j
# print(len(message), count)
plt.bar(mes_groups, counts)
plt.title('Количество действий каждой группы')
plt.show()




active_hours = [i for i in range(24)]
count_active = [0] * 24
for i in range(len(message)):
    count_active[active_hours.index(int(message[i][4][11:13]))] += 1
plt.bar(active_hours, count_active)
plt.title('Распределение активности по часам')
plt.show()




active_days = [i for i in range(1, 32)]
count_active_days = [0] * 31
for i in range(len(message)):
    count_active_days[active_days.index(int(message[i][4][8:10]))] += 1
plt.bar(active_days, count_active_days)
plt.title('Распределение активности по дням')
plt.show()




counts_correct = [0] * len(mes_groups)
j = 0
for i in range(len(results)):
    if results[i][2] == mes_groups[j]:
        if results[i][4] == '2':
            counts_correct[j] += 1
    else:
        j += 1
        if results[i][4] == '2':
            counts_correct[j] += 1
plt.bar(mes_groups, counts_correct)
plt.title('Распределение групп по количеству верно решенных задач')
plt.show()


tasks = [i for i in range(1, 6)]
counts_tasks = [0] * 5
j = 0
for i in range(len(results)):
    if results[i][4] == '2':
        counts_tasks[int(results[i][0])] += 1
plt.bar(tasks, counts_tasks)
plt.title('Количество решенных задач каждого номера')
plt.show()