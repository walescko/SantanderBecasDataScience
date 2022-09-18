cityData = {
    'nome' : 'Esteio',
    'estado' : 'Rio Grande do Sul',
    'area' : 32,
    'populacao' : 120
}

print(type(cityData))
print(cityData)

cityData['País'] = 'Brasil'
print(cityData)

cityData['area'] = 48
print(cityData)

cityData02 = cityData
cityData02['nome'] = 'Sapucaia do Sul'
print(cityData)
print(cityData02)

cityData03 = cityData.copy()
cityData03['nome'] = 'Esteio'
print(cityData)
print(cityData02)
print(cityData03)

cityNewData = {
    'populacao' : 12,
    'fundacao': '22/08/1955'
}

cityData03.update(cityNewData)
print(cityData03)

print(cityData03.get('prefeito'))

print(cityData03.keys(), "\n")
print(cityData03.values(), "\n")
print(cityData03.items(), "\n")


