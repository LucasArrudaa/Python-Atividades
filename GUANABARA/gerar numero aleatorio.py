import random
computador = random.randint(1,5) # aleatorio entre 1 a 5
palpites = []
print ('Pensei em um numero entre 1 e 5, descubra')
jogador = int(input('Em qual nunero eu pensei?'))
while jogador != computador:
    if jogador != computador: #respota do jogador for DIFERENTE da do computador
        palpites.append(jogador) #será enviado para a pasta
        print('errou, tente novamente')
        jogador = int(input('Em qual numero eu pensei?'))
else:
    jogador = computador
    print('voce acertou')
    print(f'Foram necessarios {len(palpites) + 1} palpites até o acerto') #mostrar todas tentativas de palpites



