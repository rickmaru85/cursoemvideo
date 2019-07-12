def numero(lista):
    from random import randint
    for c in range(0,5,1):
        lista.append(randint(1,10))

def pares(lista):
    soma = int(0)
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(soma)



#
lista = []
numero(lista)
print(lista)
pares(lista)

