''' Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
pares = []
impares = []
for i in range(10):
  numero = int(input('Digite um numero: '))
  if numero % 2 == 0:
    pares.append(numero)
  else:
    impares.append(numero)
print(f'{len(pares)} numeros pares e {len(impares)} numeros impares')

  