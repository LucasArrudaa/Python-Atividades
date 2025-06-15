#mostrar se é primo ou não
numero = int(input('Digite um numero: ' ))
total = 0
for primo in range ( 1, numero , + 1):
    if numero % primo == 0: # primo se mostra assim
        total += 1
print (f'O {numero} foi divisivel {total} vezes')
if total >= 2 :
    print(f'portanto não é primo')
else:
    print('Portanto é primo')



