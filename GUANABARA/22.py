masculino = 'm' or 'masculino'
feminino = 'f' or 'feminino'
while True:
    sexo = str(input('Sexo [M/F]: ')) 
    if sexo in 'Mm':
        print('Sexo masculino.')
    if sexo in 'fF':
        print('Sexo feminino.')
    else:
        print ('Opção inválida. Digite (M) para masculino ou (F) para feminino.')
