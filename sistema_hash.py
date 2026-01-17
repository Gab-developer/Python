import time
import hashlib

lista_usuarios = []
lista_senhas = []

def criar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def registrar_usuario():
    username = input("Digite seu nome de usuário: ")
    if username in lista_usuarios:
        print("Usuário já existe")
    else:
        password = input("Digite sua senha: ")
        senha = criar_hash(password)
        lista_senhas.append(senha)
        lista_usuarios.append(username)
        time.sleep(1)
        print("Registrado com sucesso!")


def logar_usuario():
    username = input("Digite seu nome de usuário: ")
    if username in lista_usuarios:
        password = input("Digite sua senha: ")
        senha = criar_hash(password)
        time.sleep(1)
        if senha in lista_senhas:
            print("Logado com sucesso!")
        else:
            print("Senha incorreta!")
    else:
        time.sleep(1)
        print("Usuário não existe!")

    
while True:
    print("\n [1] Logar \n [2] Registrar \n [3] Sair")
    pergunta = int(input("Digite sua opção: "))
    time.sleep(1)
    if pergunta == 1:
        logar_usuario()
    elif pergunta == 2:
        registrar_usuario()
    elif pergunta == 3:
        print("Saindo do programa!")
        break
