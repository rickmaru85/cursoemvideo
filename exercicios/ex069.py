pessoas_maiores    = int(0)
mulheres_menores20 = int(0)
qtd_homens         = int(0)

while True:
    idade = int(input('Digite a idade'))

    while True:
        sexo = str(input('Digite o sexo'))
        if(sexo.lower() == 'm' or sexo.lower() == 'f'):
            break

    if(idade > 21):
        pessoas_maiores += 1
    if(sexo.lower() == 'm'):
        qtd_homens += 1
    if(sexo.lower() == 'f' and idade <  20):
        mulheres_menores20 += 1

    while True:
        escolha = str(input('Deseja continuar S/N)?' ).lower())
        if(escolha.lower() == 's' or escolha.lower() == 'n'):
            break

    if(escolha.lower() == 'n'):
        break

print(f'Foi cadastrado {pessoas_maiores} maiores, {qtd_homens} homens e {mulheres_menores20} mulhere com menos de 20 anos')