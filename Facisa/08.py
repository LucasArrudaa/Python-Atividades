#8 Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua SEGUNDA nota: '))
media = (nota1 + nota2) / 2

if media >= 7.0:
    print (f'APROVADO !!!, sua media foi {media}, voce ta aprovado !!')

elif media <7:
    print (f'Voce ta reprovado, sua media é {media}')

elif media == 10:
    print (f'PARABENS, FECHOU COM A MEDIA {media}')


