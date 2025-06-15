'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita
repetir a operação para novos valores.'''

while True:
  anos = 0
  A = float(input('Digite a população do pais A: '))
  B = float(input('Digite a população do pais B: '))
  taxaCidadeA = float(input('Digite a taxa de crescimento do pais A: '))
  taxaaCidadeB = float(input('Digite a taxa de crescimento do pais B: '))
  if A > 0 and B > 0 and taxaCidadeA > 0 and taxaaCidadeB > 0:
    A = A * taxaCidadeA + A
    B = B * taxaaCidadeB + B 
    anos += 1
    if A > B:
      break

print(f'precisa de {anos} anos')
