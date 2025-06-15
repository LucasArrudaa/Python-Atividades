#ano bissesto
ano = int(input('Digite um ano: '))
bissexto = ano % 4
if bissexto == 0:
    print(f'{ano} É bissesto')
else:
    print(f'{ano} Não é bissexto')