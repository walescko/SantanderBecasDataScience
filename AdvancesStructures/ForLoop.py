print('For - loop')

cityNames = ['Esteio', 'Porto Alegre', 'Daytona', 'Varsóvia']
for name in cityNames:
    print(name)

print('\nTupla\n')
cityNames02 = 'Esteio', 'Porto Alegre', 'Daytona', 'Varsóvia'
for name in cityNames02:
    print(name)

city = {
    'name' : 'Daytona',
    'state': 'Florida',
    'population': 120.25
}

for key in city:
    print(f'{key}: {city[key]}')

for i in range(len(cityNames)):
    print(i)

for i in range(len(cityNames)):
    cityNames[i] = 'Talladega'
print(cityNames)

print(list(range(10)))
print(list(range(2, 10)))
print(list(range(2, 10, 2)))
