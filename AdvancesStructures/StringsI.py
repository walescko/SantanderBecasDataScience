company = 'Loma Linda'
print(company, type(company))

frase = "Citação: \"Vai dar erro\""
print(frase)

print(company[0])
print(company[:3])
print(company[1:4])

cityNames = 'Esteio, Floranópolis, São Paulo, Daytona'
print(cityNames)
cityNames = cityNames.split(", ")
print(cityNames)

headingMenu = '      Menu Principal     '
print(headingMenu, type(headingMenu), len(headingMenu))
print(headingMenu.strip(), type(headingMenu), len(headingMenu))

personName = 'Loma Linda produtos naturais'
print(personName)
print(personName.title())
print(personName.capitalize())
print(personName.lower())
print(personName.upper())

question = 'Qual a capital das Cucas? '
answer = 'rolante'
nameCity = input(question)
nameCity = nameCity.strip()
while nameCity.lower() != answer:
    print('Tente novamemente')
    nameCity = input(question)

print("Acertou!")

message = 'Voce viu a vitória do Logano 22 ontem?'
IhaveCited01 = 'Logano' in message
IhaveCited02 = 'Buschinho' in message
print(IhaveCited01)
print(IhaveCited02)

company = 'Walescko "loma linda"'
print(company, type(company), len(company))
