import random
valor = 0
vitorias = []
maquina = random.randint (1, 10) # gera numero aleatorio entre 1 e 10
while True:
    numero = int(input('Digite um numero:'))
    escolha = input('\nVoce escolhe par ou impar? (P/I)') .upper()
    valor = (numero + maquina)
    if  valor % 2 == 0: # se for par
        if escolha == 'P': # e ele escolher par
            vitorias.append(escolha)
            print (f'\nVOCE GANHOUU, pois a soma deu o numero {valor}\nvamos novamente !' )
        else:
            if escolha == 'I': # se ele escolher impar
                print(valor)
                break
    elif valor % 2 != 0: # se nao for par
        if escolha == 'P':  # e ele escolher par
            print(valor)
            break
        else:
            if escolha == 'I':  # e ele escolher impar
                vitorias.append(escolha)
                print(f'\nVOCE GANHOUU, o numero foi  {valor}\nvamos novamente !' )

print(f'Voce perdeu !!!\nvitorias seguidas = {len(vitorias)}\n ')






