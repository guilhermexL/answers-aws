"""
Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".
"""

def verificar_forca_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ").strip()

        if senha.lower() == "sair":
            print("Programa encerrado.")
            break

        comprimento_ok = len(senha) >= 8
        contem_numero = False

        for caractere in senha:
            if caractere.isdigit():
                contem_numero = True
                break
        if comprimento_ok and contem_numero:
            print("Senha forte! Programa encerrado.")
            break
        else:
            print("Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.\n")
verificar_forca_senha()