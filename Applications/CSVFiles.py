import csv

print('CVS File Manipulation')
with open('brasil_covid.csv', 'r') as cvsFile:
    reader = csv.reader(cvsFile)