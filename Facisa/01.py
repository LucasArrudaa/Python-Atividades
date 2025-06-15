#1 Realiza a leitura de 2 floatse imprime as seguintes operações: soma, subtração, multiplicação, divisão e resto da divisão.

numero1 = int(input ('Digite um numero: ')) 
numero2 = int(input('Digite um numero: '))

soma = numero1 + numero2
menos = numero1 - numero2
multiplo = numero1 * numero2
divisão = numero1 // numero2
resto = numero1 / numero2   

print(f'soma ={soma} subitraindo = {menos} multiplicando = {multiplo}  divisão inteira ={divisão} divisão com resto = {resto}')

