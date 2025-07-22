"""
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

- Nome do produto: "Camiseta"
- Preço original: R$ 50.00
- Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 0.20

preco_desconto = preco_original * porcentagem_desconto
preco_final = preco_original - preco_desconto

print(f"Nome do produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Porcentagem de desconto: {porcentagem_desconto * 100}%")
print(f"Valor do desconto: R$ {preco_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")