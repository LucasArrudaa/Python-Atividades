#CALCULAR O IMC

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

#CALCULO DO PESO
imc = peso / (altura * altura)
print(f'Seu imc é {round(imc,2)}')     # round ( variante, 2) mostra as casa decimais apois a virgula

#EM QUAL QUADRO ELE VAI ENTRAR
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print ('Obesidade morbida')