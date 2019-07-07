altura = float(input('digite sua altura'))
peso   = float(input('Digite seu peso'))

imc = peso / (altura**2)

if(imc <= 18.5):
    print('Abaixo do peso')
elif(imc < 25):
    print('Peso ideal')
elif(imc < 30):
    print('Sobrepeso')
elif(imc < 40):
    print('obesidade')
else:
    print('Obrsidade morbida')