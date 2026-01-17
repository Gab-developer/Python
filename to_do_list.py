lista_tarefas = []

def listar_tarefas():
    for i, tarefa in enumerate(lista_tarefas):
        print(f"{i} | {tarefa['nome']} | Prioridade: {tarefa['prioridade']}")


def criar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    prioridade = int(input("\n [1] - Alta \n [2] - Média \n [3] - Baixa \n Qual a prioridade desta tarefa?: "))
    if prioridade <= 1:
        prioridade = "Alta"
    elif prioridade == 2:
        prioridade = "Média"
    elif prioridade >= 3:
        prioridade = "Baixa"
    tarefa = {
        "nome": nome,
        "prioridade": prioridade    
    }
    lista_tarefas.append(tarefa)
    print("Tarefa criada com sucesso!")


def atualizar_tarefa():
    listar_tarefas()
    ask = int(input("Digite o id da tarefa que deseja atualizar: "))
    while True:
        ask2 = int(input("\n [1] - Nome \n [2] - Prioridade \n [3] - Sair \n O que deseja alterar?: "))
        if ask2 == 1:
            nome = input("Digite o novo nome: ")
            lista_tarefas[ask]["nome"] = nome
            print("Nome atualizado com sucesso!")

        elif ask2 == 2:
            prioridade = int(input("\n [1] - Alta \n [2] - Média \n [3] - Baixa \n Qual a nova prioridade desta tarefa?: "))
            if prioridade <= 1:
                prioridade = "Alta"
            elif prioridade == 2:
                prioridade = "Média"
            elif prioridade >= 3:
                prioridade = "Baixa"
            lista_tarefas[ask]["prioridade"] = prioridade
            print("Prioridade atualizada com sucesso!")
        
        elif ask2 == 3:
            break
            
        else:
            print("Opção não válida")


def deletar_tarefa():
    listar_tarefas()
    ask = int(input("Digite o ID da tarefa que deseja deletar: "))
    if 0 <= ask < len(lista_tarefas):
        lista_tarefas.pop(ask)
        print("Tarefa deletada com sucesso!")
    else:
        print("Tarefa não existe!")


def filtrar_prioridade():
    prioridade = int(input("\n [1] - Alta \n [2] - Média \n [3] - Baixa \n Digite a prioridade desejada: "))
    if prioridade <= 1:
        for tarefa in lista_tarefas:
            if tarefa["prioridade"] == "Alta":
                print(tarefa)
    elif prioridade == 2:
        for tarefa in lista_tarefas:
            if tarefa["prioridade"] == "Média":
                print(tarefa)
    elif prioridade >= 3:
        for tarefa in lista_tarefas:
            if tarefa["prioridade"] == "Baixa":
                print(tarefa)


def menu():
    print("""
        [1] - Listar Tarefas
        [2] - Criar Tarefa
        [3] - Atualizar Tarefa
        [4] - Deletar Tarefa
        [5] - Filtrar por prioridade
        [6] - Sair""")


while True:
    menu()
    ask = int(input("O que deseja fazer?: "))
    if ask == 1:
        listar_tarefas()
    elif ask == 2:
        criar_tarefa()
    elif ask == 3:
        atualizar_tarefa()
    elif ask == 4:
        deletar_tarefa()
    elif ask == 5:
        filtrar_prioridade()
    elif ask == 6:
        print("Finalizando o sistema!")
        break
    else:
        print("Opção inválida!")