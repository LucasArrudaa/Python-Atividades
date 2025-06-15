nome = input('digite o nome do aluno')
nota1 = float(input('digite o valor da primeira avaliação'))
nota2 = float(input('digite o valor da segunda avaliação'))
media = (nota1+nota2) / 2

if media == 10:
    print (f'{nome} Sua media igual a 10... media {media} !!!')

elif media >=7:
    print (f'{nome} Aprovado, sua media é igual a {media}')

else:
    print (f'{nome} Repovado, media {media}')