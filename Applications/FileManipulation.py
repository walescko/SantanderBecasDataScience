print('Manipulação de Arquivos')
# file = open('domcasmurro.txt', 'r')
# text = file.read()
# print(text)
# file.close()
#
# file = open('domcasmurro.txt', 'r')
# line = file.readline()
# while line != '':
#     print(line, end='')
#     line = file.readline()
# file.close()
#
# file = open('domcasmurro.txt', 'r')
# for line in file:
#     print(line, end='')
# file.close()
#
# with open('domcasmurro.txt', 'r') as file:
#     text = file.read()
#     print(text)

with open('textFile', 'w') as file:
    file.write('Primeira linha em um texto\n')
    file.write('Segunda linha em um texto\n')

with open('textFile', 'r') as file:
    print(file.read(), end='')
