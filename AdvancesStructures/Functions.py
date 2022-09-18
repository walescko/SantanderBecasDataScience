print('Functions')

def helloWorld():
    print('Hello World in function!')
helloWorld()

def AverageNumbers(a, b, c):
    average = (a + b + c)/3
    return average

result = AverageNumbers(5, 4, 6 )
print(result)

result02 = AverageNumbers(a = 2, b = 5, c =8)
print(result02)

def AverageNumbers(a = 0, b = 0, c = 0):
    average = (a + b + c)/3
    return average

result03 = AverageNumbers()
print(result03)

result04 = AverageNumbers(1, 3, 2)
print(result04)