'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''
numeros = []
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))

for i in range(num1, num2 + 1): # quero ir do num1 ao num2 sempre acrescentando 1 ( se eu colocasse + 2 seria do num1 ao num2 pulando de 2 em dois)
  numeros.append(i)
  soma = sum(numeros) - num1 - num2
print(f'{soma} sem os numeros um e numeros dois digitados')