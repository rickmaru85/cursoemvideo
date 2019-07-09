soma = int(0)
for c in range(0,6,1):
    num = int(input('digite um numero:'))
    if num % 2 == 0:
        soma += num

print(soma)