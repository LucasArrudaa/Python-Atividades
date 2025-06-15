#4 Realiza a leitura de 3 floatse imprime a média aritmética ( seria a soma dos numeros // pela quantidade de numeros)
numeros = 0
for n in range (0,3):
    numero = float(input('Digite um numero'))
    numeros = numero + numeros
media = numeros // 3
print (f'A media é {media}')
