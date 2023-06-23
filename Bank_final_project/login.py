def verifica_login():
    usuario = str(input("usuario: "))
    Senha = str(input("Senha: "))
    with open("Bank_final_project/logins.txt","r") as file:
        if f"User: {usuario} Password: {Senha}" in file.read():
            print("Login feito com sucesso!")
            import bank as BK
            BK.verificando_conta()
        else:
            if_cadastro = str(input("Usuario ou senha incorreto! Por favor pressione (1) para tentar novamente ou digite (2) para fazer o seu cadastro."))
            if if_cadastro == "1":
                verifica_login()
            elif if_cadastro == "2":
                cadastro()
            else:
                print("Comando nao encontrado")
                error()

def cadastro():
    print("Bem vindo a area de cadastro. Por gentileza seguir os seguintes passos:")
    usuario = str(input("Digite seu nome de usuario: "))
    senha = str(input("Digite a sua senha de usuario: "))
    with open("Bank_final_project/logins.txt", "a") as file:
        file.write(f"User: {usuario} Password: {senha} Tier: 1\n")
        print("Cadastro feito com sucesso!")

def deletar_login():
    print("Voce esta prestes a deletar um login! Tem certeza que deseja continuar: (1)Sim (2)Nao")
    pass
def error():
    print("Desculpe pelo mal funcionamento do codigo. Por gentileza restarte e tente novamente!")
    exit()
if __name__ == "__main__":
    verifica_login()