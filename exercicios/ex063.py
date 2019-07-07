contador = int(input('Digite a quantidade de numeros da sequencia'))

num1 = int(0)
num2 = int(1)
result = int(0)
contador -= 2
#print(contador)

print(num1)
print(num2)

while contador > 0:
    result = num1 + num2
    num1 = num2
    #print(num2)
    num2 = result
    contador -= 1
    print(result)