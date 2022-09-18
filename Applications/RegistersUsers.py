import csv

header = ['nome', 'sobrenome']
data = []
option = input('O que deseja fazer\n1 - Cadastrar\n0 - Sair\n')

while option != '0':
    name = input('Qual o nome? ')
    lastName = input('Qual o sobrenome? ')
    data.append([name, lastName])
    option = input('O que deseja fazer\n1 - Cadastrar\n0 - Sair\n')

print(data)

with open('users.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(header)
    writer.writerow(data)

with open('users.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        print(row)
