'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a populaçãode
B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

A = 80000
B = 200000
anos = 0
while True:
  A = A * 0.03 + A
  B = B * 0.015 + B
  anos += 1
  if A > B:
    break

print(f'precisam de {anos} anos')
  