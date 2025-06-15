'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores'''

numeros = []
for i in range(5):
  numero = int(input('Digite um numero: '))
  numeros.append(numero)
print(f'{min(numeros)} eh o menor numero, {max(numeros)} eh o maior numero e a soma dos numeros eh {sum(numeros)}')