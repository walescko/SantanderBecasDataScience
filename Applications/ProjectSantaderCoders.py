import csv
import urllib

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
def getDataSets(y, labels):
        if (type(y[0]) == list):
            dataSets =[]
            for i in range(len(y)):
                dataSets.append({
                    'label' : labels[i],
                    'data' : y[i]
                })
            return dataSets
        else:
            return[
                {
                    'label' : labels[0],
                    'data' : y
                }
            ]

def setTitle(title = ''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return{
        'title' : title,
        'display' : display
    }

def createChart(x, y, labels, kind='bar', title=''):
    datasets = getDataSets(y, labels)
    options = setTitle(title)

    chart = {
        'type' : kind,
        'data' : {
            'labels' : x,
            'datasets' : datasets
        },
        'options' : options
    }
    return chart

def getAPIChart(chart):
    urlBase = 'https://quickchart.io/chart'
    resp = r.get(f'{urlBase}?c={str(chart)}')
    return resp.content

def saveImage(path, content):
    with open(path, 'wb') as image:
        image.write(content)

from PIL import Image
from IPython.display import display

def displayImagem(path):
    imgPIL = Image.open(path)
    display(imgPIL)

yData01 = []
for obs in finalData[1::30]:
    yData01.append(obs[CONFIRMEDS])

yData02 = []
for obs in finalData[1::30]:
    yData02.append(obs[RECOVEREDS])

labels = ['Confirmados', 'Recuperados']

x = []
for obs in finalData[1::30]:
    x.append(obs[DATE].strftime('%d/%m/%Y'))

chart = createChart(x, [yData01, yData02], labels, title='Gráfico Confirmados vs Recuperados')
chartContent = getAPIChart(chart)
saveImage('grafico.png', chartContent)
displayImagem('grafico.png')

from urllib.parse import quote
def getAPIQRCode(link):
    text = quote(link)
    urlBase = 'https://quickchart.io/qr'
    resp = r.get(f'{urlBase}?text={text}')
    return resp.content

urlBase = 'https://quickchart.io/chart'
link = f'{urlBase}?c={str(chart)}'
saveImage('qrCode.png', getAPIQRCode(link))
displayImagem('qrCode.png')