"""
Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.

"""
import unicodedata

def verificar_palindromo():
    frase_original = input("Digite uma palavra ou frase: ")

    frase_limpa = frase_original.lower()
    
    # Remover acentos
    frase_limpa = ''.join(c for c in frase_limpa if c.isalnum())

    frase_invertida = frase_limpa[::-1]

    # Verifica se é um palíndromo
    if frase_limpa == frase_invertida:
        print("Sim")
    else:
        print("Não")
        
verificar_palindromo()