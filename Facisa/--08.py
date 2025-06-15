'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''
numeros = []
for i in range(5):
  numero = float(input('Digite um numero: '))
  numeros.append(numero)
soma = sum(numeros)
media = soma / 5
print(f'A soma dos numeros eh {soma} e a media eh {media}')