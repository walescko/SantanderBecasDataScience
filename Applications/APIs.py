import requests

print("APIs -Application Programming Interface")

url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)

print(req.status_code)

data = req.json()
print(data)

realValue = float(input('Informe o valor em R$ para conversão: R$ '))
cotation = data['rates']['BRL']
print(f'R$ {realValue} em dólar valem US$ {(realValue/cotation):.2f}')

