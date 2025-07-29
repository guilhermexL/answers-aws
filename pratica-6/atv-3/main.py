"""
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.
"""

import requests

def consultar_cep():
    
    while True:
        cep = input("Digite o CEP (apenas números, sem traço): ")

        #Validar CEP
        if not cep.isdigit() or len(cep) != 8:
            print("CEP inválido. Por favor, digite 8 dígitos numéricos.")
            continue
        break

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        
        if 'erro' in data and data['erro']:
            print(f"CEP '{cep}' não encontrado ou inválido.")
        else:
            print("\n--- Informações do Endereço ---")
            print(f"CEP: {data.get('cep', 'N/A')}")
            print(f"Logradouro: {data.get('logradouro', 'N/A')}")
            print(f"Bairro: {data.get('bairro', 'N/A')}")
            print(f"Cidade: {data.get('localidade', 'N/A')}")
            print(f"Estado: {data.get('uf', 'N/A')}")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão: Verifique sua conexão com a internet.")
    except requests.exceptions.Timeout:
        print("Erro de tempo limite: A requisição demorou muito para responder.")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição da API: {e}")
    except ValueError:
        print("Erro ao decodificar a resposta da API (formato JSON inválido).")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    consultar_cep()