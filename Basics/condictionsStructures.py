ticketValue = 4.30
runValue = float(input('Qual é o valor da corrida? '))

if runValue <= ticketValue*5:
    print('Pague a corrida!')
if runValue > ticketValue*5:
    print('Pegue o buzão')

if runValue <= ticketValue*5:
    print('Pague a corrida!')
else:
    print('Pegue o buzão')

if runValue <= ticketValue*5:
    print('Pague a corrida!')
elif runValue >= ticketValue*6:
    print('Espere um pouco, pode baixar o valor')
else:
    print('Pegue o busão')
