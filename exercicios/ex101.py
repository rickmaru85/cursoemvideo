def voto(nascimento):
    from datetime import  date
    idade = date.today().year - nascimento
    if(idade < 16):
        return 'Negado'
    elif( (16<= idade <=19) or (idade >= 65)):
        return 'Opcional'
    else:
        return 'Obrigatorio'



nasc = int(input('Digite o ano de nascimento:'))
resp = str('')
resp = voto(nasc)
print(resp)