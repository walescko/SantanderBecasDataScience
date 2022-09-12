age = input("Informe a sua idade: ") #String
print(age, type(age))
age = int(age) #mudança de tipo - quando for passível
print(age, type(age))

print(float('123.25'))
print(str(123.25))
print(bool(''))
print(bool('abc'))
print(bool(0))
print(bool(-2))

monthlySalary = input("Digite o valor do Salário Mensal: ")
monthlySpent = input("Digite o valor do gasto mensal: ")

monthlySpent = float(monthlySpent)
monthlySalary = float(monthlySalary)

totalSalary = monthlySalary*12
totalSpent = monthlySpent*12

amoutSaved = totalSalary - totalSpent

print('O montante que você pode economizar ao fim de um ano é R$ ', amoutSaved)