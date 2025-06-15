'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

numero = int(input('Digite um numero: '))
fatorial = 1
for i in range(1, numero + 1): # começa com 1 e vai ate o numero digitado subindo de um em um
  fatorial = fatorial * i # multiplica o fatorial pelo i
  print(f'{numero} x {i} = {fatorial}') # mostra a tabuada
print(f'O fatorial de {numero} eh {fatorial}') # mostra o fatorial