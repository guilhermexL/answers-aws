"""
Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.
"""
import datetime

def calcular_idade():
    try:
        ano_nascimento = int(input("Digite o ano de nascimento (ex: 1990): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o ano.")
        return
    
    ano_atual = datetime.datetime.now().year
    
    if ano_nascimento > ano_atual:
        print("O ano de nascimento não pode ser no futuro!")
        return
    elif ano_nascimento < 1900: # Um limite razoável para a idade
        print("Por favor, digite um ano de nascimento mais recente.")
        return
    
    idade_em_anos = ano_atual - ano_nascimento

    idade_em_dias = idade_em_anos * 365
    
    print(f"Você tem aproximadamente {idade_em_anos} anos.")
    print(f"Sua idade aproximada em dias é de {idade_em_dias} dias.")
calcular_idade()