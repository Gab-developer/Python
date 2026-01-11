lista_produtos = []

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço do produto: '))
    produto = {
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }
    lista_produtos.append(produto)
    print('Produto adicionado com sucesso!')

def remover_produto():
    listar_produtos()
    ask = int(input('Qual o índice do produto que deseja remover: '))
    if 0 <= ask < len(lista_produtos):
        lista_produtos.pop(ask)
        print('Produto removido com sucesso!')
    else:
        print('Índice inválido!')

def atualizar_produto():
    listar_produtos()
    ask = int(input('Qual o índice do produto que deseja remover: '))
    if 0 <= ask < len(lista_produtos):
        while True:
            print('''
            [1] - NOME
            [2] - QUANTIDADE
            [3] - PREÇO
            [4] - SAIR''')
            number = int(input('O que deseja atualizar?: '))
            if number == 1:
                nome = input('Digite o novo nome: ')
                lista_produtos[ask]['nome'] = nome
                print('Nome atualizado com sucesso!')
            elif number == 2:
                quantidade = int(input('Digite a nova quantidade: '))
                lista_produtos[ask]['quantidade'] = quantidade
                print('Quantidade atualizado com sucesso!')
            elif number == 3:
                preco = float(input('DIgite o novo preço: '))
                lista_produtos[ask]['preco'] = preco
                print('Preço atualizado com sucesso!')
            elif number == 4:
                print('Saindo de atualizações')
                break
            else:
                print('Valor não reconhecido! Tente novamente:')
    else:
        print('Índice inválido!!')

def listar_produtos():
    for indice, produto in enumerate(lista_produtos):
        print(f'{indice} | {produto['nome']} - Quantidade: {produto['quantidade']} - Preço: {produto['preco']}')

def menu():
    print('''
        [1] - Adicionar Produto
        [2] - Remover Produto
        [3] - Atualizar Produto
        [4] - Listar Produtos
        [5] - Sair''')

while True:
    menu()
    ask = int(input('O que deseja fazer?: '))
    if ask == 1:
        adicionar_produto()
    elif ask == 2:
        remover_produto()
    elif ask == 3:
        atualizar_produto()
    elif ask == 4:
        listar_produtos()
    elif ask == 5:
        print('Saindo, volte sempre!')
        break
    else:
        print('Opção inválida! Tente novamente:')