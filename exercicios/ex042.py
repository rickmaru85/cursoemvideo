lado1 = float(input('digite um lado do triangulo'))
lado2 = float(input('digite um lado do triangulo'))
lado3 = float(input('digite um lado do triangulo'))


if( lado1 > (lado2 + lado3) ):
    print('Náo é um triangulo')
else:
   if(lado2 > lado1 + lado3 ):
       print('Náo é um triangulo')
   else:
       if(lado3 > lado1 + lado2):
           print('Náo é um triangulo')
       else:
           print('é um triangulo')
           if (lado1 == lado2 and lado1 == lado3):
               print('Triangulo equilateres')
           elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
               print('Triangulo isoscels')
           else:
               print('Trianglo escaleno')

