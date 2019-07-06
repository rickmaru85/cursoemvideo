num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite o segundo numero:'))
num3 = int(input('Digite o terceiro numero:'))

if(num1 > num2):
    if(num1> num3):
        print('o maior numero é', num1 )
    else:
        print('o maior numero é' , num3)
else:
    if(num2 > num3):
        print('o Maior é o', num2)
    else:
        print('o maior é o ', num3)

if(num1 < num2):
    if(num1 < num3):
        print('o menor numero é', num1 )
    else:
        print('o menor numero é' , num3)
else:
    if(num2 < num3):
        print('o menor é o', num2)
    else:
        print('o menor é o ', num3)
