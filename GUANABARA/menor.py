#PODE OU NAO SER UM TRINAGULO
r1 = float(input('Digite um lado do triangulo: '))
r2 = float(input('Digite o segundo lado do triangulo: '))
r3 = float(input('Digite o terceiro lado do triangulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É um triangulo !')

    # QUAL TIPO DE TRIANGULO
if r1 == r2 == r3:
    print('EQUILATERO')

elif r1 != r2 != r3 != r1:
    print('ESCALENO')
    
else:
    print('escaleno')

