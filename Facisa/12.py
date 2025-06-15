'''12 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média. A atribuição de conceitos deve obedecer à tabela acima.'''

nota1 = float(input('Digite sua PRIMEIRA nota: '))
nota2 = float(input('Digite sua SEGUNDA nota: '))
media = (nota1 + nota2) // 2

if media <=4 : # MENOR OU IGUAL A 4
    print (F' sua media foi {media} NOTA E, REPROVADO')

elif media >4 and media <= 6: # MAIOR QUE 4 E MENOR OU IGUAL 6
    print (F' sua media foi {media} NOTA D, RECUPERAÇÃO ')

elif media >= 6.1 and media <= 7.5 : #MAIOR QUE 6 E MENOR OU IGUAL 7.5 
    print (F' sua media foi {media} NOTA C')

elif media >= 7.6 and media <= 9 : # MAIOR Q 7.5 E MENOR OU IGUAL A 9
    print (F' sua media foi {media} NOTA B, BOA')

elif media >= 9.1 and media == 10:
     print (F' sua media foi {media} NOTA A, OTIMA NOTA ') 