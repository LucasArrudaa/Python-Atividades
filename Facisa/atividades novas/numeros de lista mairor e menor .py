numeros = [32,10,58,30,55,12,28,51]
def maioreMenor(numeros):
    maior = numeros[0]
    menor = numeros[0]
    for numero in numeros: #para cada numero na lista
        if numero > maior: #se o numero for maior que o maior
            maior = numero
        if numero < menor: #se o numero for menor que o menor
            menor = numero
    return maior, menor  #retorna o maior e o menor

maior, menor = maioreMenor(numeros) #   chamando a funcao
print(maior, menor)

