print('Functions - II - Arrays')
def AverageCalc(*args):
    print(args, type(args))

AverageCalc(10, 80, 8)

def AverageCalc(*args):
    sum01 = sum(args)
    average = sum01/len(args)
    return average

print(AverageCalc(2, 3, 4))

def AverageCalc(*args, marge):
    sum01 = sum(args)
    average = sum01/len(args)
    return average + marge
print(AverageCalc(2, 3, 4, marge=0.1))

def printInfo(**kwargs):
    print(kwargs, type(kwargs))

printInfo(nome = 'Walescko', sobrenome = 'chimendes')




