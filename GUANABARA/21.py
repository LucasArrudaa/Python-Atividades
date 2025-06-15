while True: #ENQUANTO O INPUT r RECEBER A LETRA S, O WHILE VAI RODANDO
    numero = int(input('Digite um numero: '))
    print(numero)
    resposta= str(input('Quer continuar? [S/N] ')).upper() #SE RECEBER N ELE PARA E VAI PRO PRINT
    if resposta == 'N' :
        print('fim')
        break