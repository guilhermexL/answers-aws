"""
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""

import requests
from datetime import datetime

def consultar_cotacao_moeda():
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").upper()

    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        chave_moeda = f"{moeda}BRL"

        if chave_moeda not in data:
            print(f"Código de moeda '{moeda}' inválido ou não encontrado. Verifique se o código está correto (ex: USD, EUR, GBP).")
            return

        cotacao = data[chave_moeda]

        # Conversão para data/hora legível
        timestamp = int(cotacao['timestamp'])
        data_hora_atualizacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        print(f"\n--- Cotação de {moeda}/BRL ---")
        print(f"Moeda: {cotacao['name']}")
        print(f"Cotação Atual (Compra): R$ {float(cotacao['bid']):.2f}")
        print(f"Cotação Atual (Venda): R$ {float(cotacao['ask']):.2f}")
        print(f"Valor Máximo (Dia): R$ {float(cotacao['high']):.2f}")
        print(f"Valor Mínimo (Dia): R$ {float(cotacao['low']):.2f}")
        print(f"Data/Hora da Última Atualização: {data_hora_atualizacao}")

    except requests.exceptions.ConnectionError:
        print("Erro de conexão: Verifique sua conexão com a internet.")
    except requests.exceptions.Timeout:
        print("Erro de tempo limite: A requisição demorou muito para responder.")
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição da API: {e}")
    except ValueError:
        print("Erro ao decodificar a resposta da API. O formato JSON pode estar inválido.")
    except KeyError:
        print(f"Erro ao processar os dados da API para '{moeda}'. A estrutura da resposta pode ter mudado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    consultar_cotacao_moeda()