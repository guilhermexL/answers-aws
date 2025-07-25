"""
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.
"""
pergunta = int(input("Começar (1 = Sim e 0 = Não): "))

while pergunta == 1:

    valor1 = int(input("Insira um valor: "))
    valor2 = int(input("Insira outra valor: "))

    escolha = input("Qual operação você deseja(apenas o símbolo): ")

    if valor1 == 0 and valor2 == 0:
        print("Cálculo impossível")
    else:
        if escolha == "+":
            soma = valor1 + valor2
            print(f"{valor1} + {valor2} = {soma}")
        elif escolha == "-":
            subtracao = valor1 - valor2
            print(f"{valor1} - {valor2} = {subtracao}")
        elif escolha == "*":
            multiplica = valor1 * valor2
            print(f"{valor1} * {valor2} = {multiplica}")
        elif escolha == "/":
            if valor2 == 0:
                print("Divisão por 0, não rola")
            else:
                divide = valor1 / valor2
                print(f"{valor1} / {valor2} = {divide}")
    pergunta = int(input("Deseja fazer outro cálculo? (1 = Sim, 0 = Não): "))
print("Fim da excução")