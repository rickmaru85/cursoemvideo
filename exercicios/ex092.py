from datetime import date


pessoa = {}

pessoa['nome'] = str(input('Digite o nome:'))
pessoa['idade'] = int(date.today().year - int(input('Digite o ano de nascimento')))
pessoa['ctps'] = int(input('Digite a ctps;'))

if pessoa['ctps'] != 0:
    pessoa['contração'] = int(input('Digite o ano de contratação:'))
    pessoa['salario'] = int(input('Digite o salario:R$'))
    pessoa['aposentadoria'] = ((int(pessoa['contração'])+int(35))-(int(date.today().year) - int(pessoa['idade'])))

for k,v in pessoa.items():
    print(f'{k} tem o valor de {v}')