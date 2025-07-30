'''
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.
'''

import csv

def criar_e_salvar_csv():

    dados_pessoas = [
        ["Nome", "Idade", "Cidade"],
        ["Maria Silva", 30, "São Paulo"],
        ["João Santos", 25, "Rio de Janeiro"],
        ["Ana Oliveira", 40, "Belo Horizonte"]
    ]

    nome_arquivo = input("Por favor, digite o nome do arquivo CSV para salvar (ex: pessoas.csv): ")

    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            for linha in dados_pessoas:
                writer.writerow(linha)
        print(f"\nDados salvos com sucesso no arquivo '{nome_arquivo}'!")

    except IOError as e:
        print(f"\nErro de E/S ao tentar escrever no arquivo '{nome_arquivo}': {e}")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

criar_e_salvar_csv()