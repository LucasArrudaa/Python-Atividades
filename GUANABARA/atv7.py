#CALCULAR LADOS DE UM SUPOSTO TRIANGULO

r1 = float(input('Digite um lado do triangulo: '))
r2 = float(input('Digite um lado do triangulo: '))
r3 = float(input('Digite um lado do triangulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('PODEM FORMAR UM TRIÂNGULO')
else:
    print('NÃO PODEM FORMAR UM TRIÂNGULO')
