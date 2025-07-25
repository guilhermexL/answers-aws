"""
Analisador de Números Pares e Ímpares
Desenvolva um programa que classifica números inteiros como pares ou ímpares. O programa deve:

* Solicitar números inteiros até que o usuário digite "fim".  
* Informar se o número digitado é par ou ímpar.  
* Ao final, exibir a quantidade total de números pares e ímpares informados.  
* Tratar entradas inválidas com mensagens de erro apropriadas.  
"""

def analisar_pares_impares():
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip().lower()

        if entrada == "fim":
            break

        if entrada.lstrip("-").isdigit():
            numero = int(entrada)
            if numero % 2 == 0:
                print("Número par.")
                pares += 1
            else:
                print("Número ímpar.")
                impares += 1
        else:
            print("Erro: entrada inválida. Digite um número inteiro ou 'fim'.")
            
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

analisar_pares_impares()