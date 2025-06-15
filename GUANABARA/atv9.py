#numeros e quais sao maiores ou menores
a = int(input('Digite um numero: '))
b = int(input('Digite um numero: '))
c = int(input('Digite um numero: '))
#verificar quem é menor
menor = a
if b<a and b<c:
    menor = b
elif c<a and c<b:
 menor = c
 #o maior agora
 maior = b
 if b>a and b>c:
     maior = b
elif c>a and c<b:
    maior = c

print(f'{menor} menor')
print(f'{maior} maior')