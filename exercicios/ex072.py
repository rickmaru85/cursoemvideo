a = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze')
b = ('treze','catorze','quinze','dezeseis','dezessete','dezoito','dezenove','vinte')

numeros = a + b

while True:
    digitado = int(input('Digite um numero entre 0 e 20:'))
    if(0 < digitado < 20):
        break

print(numeros[digitado])
