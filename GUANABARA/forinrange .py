soma = 0
for c in range ( 0, 6 ): # GERA DE 1 A 6
    numero = int(input('Digite um numero :'))
    if numero % 2 == 0:                 #em python, identificamos um numero PAR assim
        soma = soma + numero
print (f'A soma dos numeros pares deu {soma}')
