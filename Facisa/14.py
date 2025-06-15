sexualidade = str(input('Digite a LETRA do seu sexualidade ( M / F )' )) .strip() .upper()[0] 
# upper deixa a letra maiuscula e o strip retira os espaços em branco


if sexualidade == 'M' :
    print ('sexualidade Masculino')


elif sexualidade == 'F':
    print ('sexualidade Femino')
    
        
elif sexualidade != 'M' and sexualidade != 'F':
        print ('Digite uma opção vallida ( M / F )')
        