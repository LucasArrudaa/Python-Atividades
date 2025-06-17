''' faça dois def, um que recebe uma string e retorna a string invertida,'''

def inverter_string(s):
    return s[::-1]  # Inverte a string usando slicing, slicing é uma técnica de Python para acessar partes de sequências como strings, listas, etc.

# Testando as funções

string = input("Digite uma frase : ")
print(f"String original: {string}")
print(f"String invertida: {inverter_string(string)}")
