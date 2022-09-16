countryNames = ['Brasil', 'Argentina', 'Estados Unidos', 'Canadá', 'Japão']
print(countryNames)

print('Tamanho da lista:', len(countryNames))

print('País', countryNames[4])
print('País', countryNames[-1])

countryNames[4] = 'Polônia'

print('Países', countryNames)
print('País: ', countryNames[4])
# Slice
print(countryNames[1:3])
print(countryNames[1:-1])
print(countryNames[1:])
print(countryNames[:3])
print(countryNames[:])
print(countryNames[::2])
print(countryNames[::-1])

print('Brasil' in countryNames)
print('Canada' not in countryNames)

cityList = []



