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

def resumo(preco = 0,aumento = 10,reducao = 10):
    print('-'*40)
    print(f'{"Resumo do valor":^40}')
    print('-' * 40)
    print(f'Preco analisado: {moeda(preco):>23}')
    print(f'dobro do preco : {dobro(preco,True):>23} ')
    print(f'a medae do preco: {metade(preco,True):>22}')
    print(f'{aumento:<3}% de aumento: {aumenta(preco,aumento,True):>23}')
    print(f'{reducao:<3}% de reducao: {diminui(preco,reducao,True):>23}')
    print('-'*40)
