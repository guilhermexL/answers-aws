"""
Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

peso = float(input("Digite seu peso: ") or 0)
altura = float(input("Digite sua altura: ") or 0)
imc = peso / (altura ** 2)
classificacao = "Abaixo do peso" if imc < 18.5 else "Peso normal" if imc < 25 else "Sobrepeso" if imc < 30 else "Obeso"
print(f"Classificação: {classificacao}")