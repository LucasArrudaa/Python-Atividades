#formas de pagamento de um produto

pagamento = float (input ('Qual o valor do produto? ')) # se responder fora das opção ( no caso, o else ), recomeça o codigo  daqui
print('Qual a forma de pagamento:\n1: à vista\n2: cartão à vista\n3: cartão em 2x\n4: cartão em 3x\n ')
forma_de_pagamento = input ('Qual a forma de pagamento? ')

forma_de_pagamento != 4 
    # calculos de cada função
if forma_de_pagamento == '1': # á vista
    novo_valor = pagamento * 0.10 #dez %
    novo_valor = pagamento - novo_valor
    print(f'O valor fica de R$ {novo_valor} a vista em dinheiro ou pix')
    

elif forma_de_pagamento == '2': # cartão a vista
    novo_valor = pagamento * 0.05 # 5%
    novo_valor = pagamento + novo_valor
    print(f'O valor fica de R$ {novo_valor} a vista no cartão')
        

elif forma_de_pagamento == '3':# cartao em 2x
    parcela = pagamento // 2
    print(f'O valor fica o mesmo de R${pagamento} em 2x')
    print(f'{parcela} o valor da parcela ')
        

elif forma_de_pagamento == '4': #cartao em 3x
    novo_valor = pagamento * 0.20
    novo_valor = pagamento + novo_valor
    parcela = pagamento // 3
    print(f'O valor fica de R$ {novo_valor} em 3x')
    print(f'{parcela} o valor da parcela ')
       
else: #qualquer outra alternativa que não exista
    print('Não existe essa possibilidade de escolha !! TENTE NOVAMENTE ') 
        
''' OUTRA MANEIRA DE FAZER O MESMO CODIGO 
        
        #formas de pagamento de um produto
while True:
    pagamento = float (input ('Qual o valor do produto? ')) # se responder fora das opção ( no caso, o else ), recomeça o codigo  daqui
    while True:
        print('Qual a forma de pagamento:\n1: à vista\n2: cartão à vista\n3: cartão em 2x\n4: cartão em 3x\n ')
        forma_de_pagamento = input ('Qual a forma de pagamento? ')
        # calculos de cada função
        if forma_de_pagamento == '1': # á vista
            novo_valor = pagamento * 0.10
            novo_valor = pagamento - novo_valor
            print(f'O valor fica de R$ {novo_valor} a vista em dinheiro ou pix')
            break # para quando responder, pedir valor e opção dnv 
        elif forma_de_pagamento == '2': # cartão a vista
            novo_valor = pagamento * 0.05
            novo_valor = pagamento + novo_valor
            print(f'O valor fica de R$ {novo_valor} a vista no cartão')
            break# para quando responder, pedir valor e opção dnv 
        elif forma_de_pagamento == '3':# cartao em 2x
            print(f'O valor fica o mesmo de R${pagamento} em 2x')
            break# para quando responder, pedir valor e opção dnv 
        elif forma_de_pagamento == '4': #cartao em 3x
            novo_valor = pagamento * 0.20
            novo_valor = pagamento + novo_valor
            print(f'O valor fica de R$ {novo_valor} em 3x')
            break# para quando responder, pedir valor e opção dnv 
        else: #qualquer outra alternativa que não exista
            print('Não existe essa possibilidade de escolha !! TENTE NOVAMENTE ')'''
            
            

