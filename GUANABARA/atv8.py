#salario
salario = float(input('Digite seu salario: '))

if salario <= 1250 :
    salario =  salario * 0.10 + salario #0.10 = 10%
    print(f'{salario}')
    
else:
    salario * 0.15 + salario
    print(f'{salario}')