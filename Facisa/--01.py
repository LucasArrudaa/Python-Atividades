''''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
usuário informe um valor válido.'''

while True:
  numero = int(input('Digite a sua nota aqui: '))
  if numero <= 10 and numero >= 0:
    print(f'Nota {numero} aceita')
    break
  else:
    print('Nota ivalida, tente novamente')
print('go')