def metade(preco  = 0,formata = False):
    res = preco/2
    if formata == True:
        res = moeda(res)
    return res

def dobro(preco = 0,formata = False):
    res = preco*2
    if formata == True:
        res = moeda(res)
    return res

def aumenta(preco = 0,taxa = 0, formata = False):
    res = preco + (preco*taxa/100)
    if formata == True:
        res = moeda(res)
    return res

def diminui(preco = 0,taxa = 0, formata = False):
    res = preco - (preco*taxa/100)

    if formata == True:
        res = moeda(res)
    return res

def moeda(preco = 0,moeda = 'R$'):
    return f'{moeda}{preco:0.2f}'.replace('.',',')
