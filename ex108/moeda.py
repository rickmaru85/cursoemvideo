def metade(preco  = 0):
    res = preco/2
    return res

def dobro(preco = 0):
    res = preco*2
    return res

def aumenta(preco = 0,taxa = 0):
    res = preco + (preco*taxa/100)
    return res

def diminui(preco = 0,taxa = 0):
    res = preco - (preco*taxa/100)
    return res

def moeda(preco = 0,moeda = 'R$'):
    return f'{moeda}{preco:0.2f}'.replace('.',',')
