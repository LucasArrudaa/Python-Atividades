frase = str(input('Digite qualquer frase ou palavra: '))
palavras = frase.split() # separar as palavras
junto = ''.join(palavras) #juntas as palavras
inverso ='' # len(junto) len de letra e junto seria a ultima letra das palavras
for letra in range (len(junto)-1, -1 , -1): # primeiro -1 serve para ir até o final
    inverso += junto[letra]                 #segundo - 1 para ir antes da ultima letra, ou seja, começo
if junto == inverso:                         # -1 por terceiro ir voltando
    print('polindromo')
else:
    print('Não polindromo')









