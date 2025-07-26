"""
Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""

def calculadora_desconto():
    # Valor do produto
    try:
        preco_original = float(input("Digite o preço original do produto (ex: 100.50): R$ "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o preço.")
        return
    
    # Solitar porcentagem de disconto
    try:
        percentual_desconto = float(input("Digite o percentual de desconto desejado (ex: 10, 25.5): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número para o percentual de desconto.")
        return
    
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    
    print(f"Preço Original: R$ {preco_original:.2f}")
    print(f"Percentual de Desconto: {percentual_desconto:.2f}%")
    print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
    print(f"Preço Final com Desconto: R$ {preco_final:.2f}")
calculadora_desconto()