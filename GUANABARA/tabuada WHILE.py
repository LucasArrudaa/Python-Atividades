tabuada = []
while True:
    print('Se digitar qualquer numero menor do que 0, o program fecha: ')
    numero = int(input('Digite um numero :'))
    if numero < -1: # se for numero negativo, cancela o prgorama
        break
    elif numero >= 0: # maior ou igual que 0 ele gera a tabuada 
        for i in range(1,11):
            tabuada = numero * i
            print(f'{numero} x {i} = {tabuada}')


