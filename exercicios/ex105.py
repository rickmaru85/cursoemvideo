def notas(*nota,sit = False):
    classe = {}
    classe['total'] = len(nota)
    maior = menor  = soma = float(0)
    for pos,n in enumerate(nota):
        if(pos == 0):
            menor = maior = n
        else:
            if(n > maior):
                maior = n
            if(n < menor):
                menor = n
        soma += float(n)
        media = soma/len(nota)
    classe['maior'] = maior
    classe['menor'] = menor
    classe['media'] = media
    if(sit == True):
        if(media < 5):
            classe['sit'] = 'Ruim'
        elif(5 < media < 7):
            classe['sit'] = 'Razoavel'
        elif(7 < media < 9):
            classe['sit'] = 'Otimo'
    return classe


turma = {}
turma = notas(5.5,9.0,3,9.5,sit= True)
print(turma)



