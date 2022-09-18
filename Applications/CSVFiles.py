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
