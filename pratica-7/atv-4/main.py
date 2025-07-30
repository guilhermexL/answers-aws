'''
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
'''

import json
import os

def manipular_json_pessoa():
   
    dados_pessoa = {
        "nome": "Guilherme Santos",
        "idade": 27,
        "cidade": "Campina Grande"
    }

    nome_arquivo = input("Por favor, digite o nome do arquivo JSON (ex: pessoa.json): ")

    # --- Salvar os dados em JSON ---
    print(f"\nTentando salvar dados no arquivo '{nome_arquivo}'...")
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_pessoa, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em '{nome_arquivo}'.")
    except IOError as e:
        print(f"Erro de E/S ao tentar escrever no arquivo '{nome_arquivo}': {e}")
        return
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao salvar o arquivo: {e}")
        return

    # --- Ler os dados do arquivo JSON ---
    print(f"\nTentando ler dados do arquivo '{nome_arquivo}'...")
    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado para leitura.")
        return

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados_carregados = json.load(f)
        print("Dados carregados com sucesso:")
        print(dados_carregados)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON do arquivo '{nome_arquivo}'. O arquivo pode estar corrompido: {e}")
    except IOError as e:
        print(f"Erro de E/S ao tentar ler o arquivo '{nome_arquivo}': {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao ler o arquivo: {e}")

manipular_json_pessoa()