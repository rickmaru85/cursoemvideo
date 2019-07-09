 qtd_prd_mais_mil      = int(0)
nome_prod_mais_barato = str('')
preco_mais_barato     = float(0)
tot_compra            = int(0)

while True:
    nome_prd = str(input('Digite o nome do produto:'))
    preco = float(input('Digite o preço do produto:'))

    tot_compra += preco

    if(preco > 1000):
        qtd_prd_mais_mil += 1

    if( preco < preco_mais_barato or nome_prod_mais_barato == ''):
        nome_prod_mais_barato = nome_prd

    while True:
        escolha = str(input('Deseja continuar?(S/N)'))
        if(escolha.lower() == 's' or escolha.lower() == 'n'):
            break
    if(escolha.lower() == 'n'):
         break

print(f'O total da compra foi {tot_compra:0.2f}, fora selecionados {qtd_prd_mais_mil} produtos com valor maior que 1000')
print(f'O produto mais barato foi {nome_prod_mais_barato}')