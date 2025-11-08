tarefas = []

def adicionar_tarefas():
    titulo = input("Título da tarefa: ")
    categoria = input("Categoria: ")
    prioridade = input("Prioridade [alta, média, baixa]:")

    tarefa = {
        "titulo": titulo,
        "categoria": categoria,
        "prioridade": prioridade
    }
    tarefas.append(tarefa)
    print(f'Tarefa "{titulo}" adicionada!')

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada. \n")
        return
    print("\n=== LISTA DE TAREFAS ===")
    for i, t in enumerate(tarefas, start=1):
        print(f"{i}. {t['titulo']} | Categoria: {t['categoria']} | Prioridade: {t['prioridade']}")
        print()
    
def mostrar_filtradas(lista):
    if not lista:
        print("Nenhuma tarefa encontrada com esse filtro.\n")
    else:
        for t in lista:
            print(f"- {t['titulo']} ({t['categoria']}, prioridade {t['prioridade']})")
        print()

def filtrar_por_categoria():
    cat = input("Digite a categoria para filtrar: ")
    filtradas = [t for t in tarefas if t['categoria'].lower() == cat.lower()]
    mostrar_filtradas(filtradas)

def filtrar_por_prioridade():
    prio = input("Digite a prioridade para filtrar: ")
    filtradas = [t for t in tarefas if t['prioridade'].lower() == prio.lower()]
    mostrar_filtradas(filtradas)

def remover_tarefa():
    listar_tarefas()
    num = int(input("Número da tarefa que deseja remover: ")) - 1
    if 0 <= num < len(tarefas):
        removida = tarefas.pop(num)
        print("Tarefa removida com sucesso!")
    else:
        print("Número invállido. \n")

def sair():
    print("Saindo.. Até logo!")
    exit()

def menu():
    opcoes = {
        "1": adicionar_tarefas,
        "2": listar_tarefas,
        "3": filtrar_por_categoria,
        "4": filtrar_por_prioridade,
        "5": remover_tarefa,
        "0": sair,
    }

    while True:
        print("""
    === GERENCIADOR DE TAREFAS ===
    1. Adicionar tarefas
    2. Listar tarefas
    3. Filtrar por categoria
    4. Filtrar por prioridade
    5. Remover tarefas
    0. Sair
    """)
        
        escolha = input("Escolha uma ação: ")
        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("Opção inválida. \n")

if __name__ == "__main__":
    menu()

