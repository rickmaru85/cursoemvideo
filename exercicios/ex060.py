numero = int(input('Digite um numero'))

fatorial = int(0)

while numero > 0:
    if fatorial == 0:
        fatorial = numero
    else:
        fatorial *= numero
    numero -= 1

print('O fatorial é',fatorial)