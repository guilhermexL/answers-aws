"""
Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais.
"""

def calculadora_gorgeta():
    conta = float(input("Digite o valor da conta: R$ "))
    porcentagem_gorjeta = int(input("Deseja dar 10%, 15% ou 20% de gorjeta? Digite apenas o número: "))
    
    valor_gorjeta = 0

    if porcentagem_gorjeta == 10:
        valor_gorjeta = conta * (10 / 100)
        print(f"Você escolheu 10% de gorjeta.")
    elif porcentagem_gorjeta == 15:
        valor_gorjeta = conta * (15 / 100)
        print(f"Você escolheu 15% de gorjeta.")
    elif porcentagem_gorjeta == 20:
        valor_gorjeta = conta * (20 / 100)
        print(f"Você escolheu 20% de gorjeta.")
    else:
        print("Opção de gorjeta inválida ou o cliente recusou pagar a gorjeta.")
        print(f"O valor a ser pago é apenas o total da conta: R$ {conta:.2f}")
        return
    
    total_a_pagar = conta + valor_gorjeta
    
    print(f"Valor da conta: R$ {conta:.2f}")
    print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
    print(f"Total a pagar: R$ {total_a_pagar:.2f}")
calculadora_gorgeta()