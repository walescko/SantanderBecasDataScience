print('Manipulação de Arquivos')
file = open('domcasmurro.txt', 'r')
text = file.read()
print(text)
file.close()

file = open('domcasmurro.txt', 'r')
line = file.readline()
while line != '':
    print(line, end='')
    line = file.readline()

file.close()