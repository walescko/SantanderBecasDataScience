#single while
count = 0
while count < 10:
    count = count + 1
    if count == 1:
        print(count, " elemento")
    else:
        print(count, " elementos")
print('Fim do bloco 1')

#while with True and break
count = 0
while True:
    if count < 10:
        count += 1
        if count == 1:
            print(count, " elemento")
        else:
            print(count, " elementos")
    else:
        break
print('Fim do bloco 2')

#while with control acess

text = input('Digite o código de acesso: ')

while text != "acesso":
    text = input('Acesso negado. Tente novamente: ')

print('Acesso liberado')
print('Fim do bloco 3')

#while with continue
count = 0
while count < 10:
    count = count + 1
    if count == 1:
        continue
    print(count, " elementos")
print('Fim do bloco 4')
