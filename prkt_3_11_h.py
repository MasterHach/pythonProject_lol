import csv
import datetime
import requests
import matplotlib.pyplot as plt
import pandas as pd




def lolik():
    lol_1 = 'https://raw.githubusercontent.com/true-grue/kispython'
    lol_2 = '/main/data/messages.csv'
    lol_3 = 'https://raw.githubusercontent.com/Newbilius/Old-Games_DOS_Game_Gauntlet/master/GAMES.csv'
    response = requests.get(f'{lol_3}').text.splitlines()
    stream = csv.reader(response)
    return list(stream)


j = 0
years = []
mes = lolik()
for i in mes:
    temple_str = ''.join(i).split(';')
    if temple_str[3].strip('"') != "не издана":
        if int(temple_str[3].strip('"')) not in years:
            years.append(int(temple_str[3].strip('"')))
popular = [0] * len(years)
for i in mes:
    temple_str = ''.join(i).split(';')
    if temple_str[3].strip('"') != "не издана":
        if years[j] == int(temple_str[3].strip('"')):
            popular[j] += 1
        else:
            j += 1
            popular[j] += 1
plt.bar([str(i) for i in years], popular)
# plt.title('Распределение игр по популряности выхода')
plt.show()


themes = []
for i in mes:
    temple_str = ''.join(i).split(';')
    if temple_str[1].strip('"') not in themes:
        themes.append(temple_str[1].strip('"'))
data = {i: [0] * len(years) for i in sorted(themes)}
print(data)
for i in mes:
    temple_str = ''.join(i).split(';')
    if temple_str[3].strip('"') != "не издана":
        data[temple_str[1].strip('"')][years.index(int(temple_str[3].strip('"')))] += 1
print(years)
df = pd.DataFrame(data)
for k, v in data.items():
    plt.plot(years, v, label=k)
plt.legend(data, loc = 2)
plt.show()