numero = int(input('Digite um numero inteiro'))
conversao = int(input('Digite 1 para converter em binario 2 em octal ou 3 em hexa'))


if(conversao == 1):
    print(bin(numero).format(30)[2:])
elif(conversao == 2):
    print(oct(numero)[2:])
else:
    print(hex(numero)[2:])