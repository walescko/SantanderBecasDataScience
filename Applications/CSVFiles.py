import csv

print('CVS File Manipulation')
with open('brasil_covid.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for line in reader:
        print(line)

with open('brasil_covid.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    header = next(reader)
    for line in reader:
        if float(line[3])>1:
            print(line)

with open('brasil_covid.csv', 'r') as csvFile:
    lines = csvFile.read()
    lines = lines.split('\n')
    for line in lines:
        line = line.split(',')
        print(line)

with open('users.csv', 'w', newline='') as usersFile:
    writer = csv.writer(usersFile)
    writer.writerow(['nome', 'sobrenome', 'email', 'genero'])
    writer.writerow(['Joey', 'Logano', 'logano@nascar.com', 'male'])

with open('users.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for line in reader:
        print(line)
