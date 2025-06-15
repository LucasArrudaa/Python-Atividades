
#soma de apenas numeros pares colocados aqui
soma = 0
for c in range ( 0, 6 ):
    numero = int(input('Digite um numero :'))
    if numero % 2 == 0: #             em python, identificamos um numero PAR assim
        soma = soma + numero
print(soma)