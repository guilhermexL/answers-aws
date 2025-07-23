"""
Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

- Criança (0-12 anos), 
- Adolescente (13-17 anos), 
- Adulto (18-59 anos) ou 
- Idoso (60 anos ou mais).
"""

idade = int(input("Digite sua idade: ") or 0)
categoria = "Criança" if idade <= 12 else "Adolescente" if idade <= 17 else "Adulto" if idade <= 59 else "Idoso"
print(f"Categoria: {categoria}")