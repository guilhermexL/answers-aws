"""
Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temperatura = float(input("Digite a temperatura: ") or 0)
unidade_origem = input("Digite a unidade de origem (C, F ou K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F ou K): ").upper()

if unidade_origem == "C":
    if unidade_destino == "F":
        temperatura_convertida = (temperatura * 9/5) + 32
    elif unidade_destino == "K":
        temperatura_convertida = temperatura + 273.15
    else:
        temperatura_convertida = temperatura
elif unidade_origem == "F":
    if unidade_destino == "C":
        temperatura_convertida = (temperatura - 32) * 5/9
    elif unidade_destino == "K":
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
    else:
        temperatura_convertida = temperatura
        print(temperatura_convertida)
elif unidade_origem == "K":
    if unidade_destino == "C":
        temperatura_convertida = temperatura - 273.15
    elif unidade_destino == "F":
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
    else:
        temperatura_convertida = temperatura
else:
    temperatura_convertida = temperatura

print(f"Temperatura convertida: {temperatura_convertida} {unidade_destino}")