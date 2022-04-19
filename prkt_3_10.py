import csv
import datetime
import requests

def kekster(a):
    return a[3]

def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


def lolik():
    lol_1 = 'https://raw.githubusercontent.com/true-grue/kispython'
    lol_2 = '/main/data/messages.csv'
    response = requests.get(f'{lol_1}{lol_2}').text.splitlines()
    stream = csv.reader(response)
    return list(stream)


# with open('data/messages.csv', encoding='utf8') as f:
#     messages = list(csv.reader(f, delimiter=','))
# with open('data/results.csv', encoding='utf8') as f:
#     results = list(csv.reader(f, delimiter=','))
message = lolik()
message.sort(key=kekster)
for i in message:
    print(i)
