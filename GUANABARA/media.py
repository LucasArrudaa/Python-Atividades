'''#MEDIA DO ALUNO
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota:' ))
media = (nota1 + nota2 ) // 2
print (f'Sua media foi de {media}')
#INFORMAÇÃO DE ACORDO COM A NOTA
if media >= 7.0: # maior ou igual a 
    print('Aprovado')
elif media > 5.0 and media < 6.9:
    print('recuperação')
else:
    print('Reprovado, melhore !!!!')'''
notas = [] 

def calculo_media ():
    for n in range(2):
        nota = float(input('Digite sua primeira nota: '))
        notas.append(nota)
    media = sum(notas) / len(notas)
    print(f'Sua media foi de {media}')

    if media >= 7.0 and media <= 10.0:
        print('Aprovado')   
    elif media >= 5.0 and media <= 6.9:
        print('Recuperação')
    elif media > 10.0:
        print('Nota inválida') 
    else:       
        print('Reprovado, melhore !!!!')

    return media

media = calculo_media()
print(media)
        

