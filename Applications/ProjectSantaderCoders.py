import csv

import requests as r
import datetime

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)
print(resp.status_code)

rawData = resp.json()
# print(rawData[0])

finalData = []
for obs in rawData:
    finalData.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

finalData.insert(0, ['Confirmados', 'óbitos', 'recuperados', 'ativos', 'data'])

CONFIRMEDS = 0
DEATHS = 1
RECOVEREDS = 2
ACTIVES = 3
DATE = 4

for i in range(1, len(finalData)):
    finalData[i][DATE] = finalData[i][DATE][:10]

with open('brazilianCovid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(finalData)

for i in range(1, len(finalData)):
    finalData[i][DATE] = datetime.datetime.strptime(finalData[i][DATE],'%Y-%m-%d')


print(finalData)