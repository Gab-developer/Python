def menu():
    print("Bem vindo a calculadora!")
    print("""
    [1] Somar
    [2] Subtrair
    [3] Multiplicar
    [4] Dividir""")

def somar(n1, n2):
    soma = n1 +  n2
    print(f"A soma entre {n1} e {n2} é {soma}")

def subtrair(n1, n2):
    if n1 < n2:
        pergunta = int(input("O número que você digitou primeiro é maior que o segundo, deseja continuar mesmo assim? [1] Sim / [2] Não: "))
        if pergunta == 1:
            sub = n1 - n2
            print(f"A subtração entre {n1} e {n2} é {sub}")
        elif pergunta == 2:
            print("Finalizando...")
    elif n1 > n2:
        sub = n1 - n2
        print(f"A subtração entre {n1} e {n2} é {sub}")
    else:
        print(f"A subtração entre {n1} e {n2} é 0")
    
def multiplicar(n1, n2):
    multi = n1 * n2
    print(f"A multiplicação entre {n1} e {n2} é {multi}")

def dividir(n1, n2):
    if n1 < n2:
        pergunta = int(input("O número que você digitou primeiro é maior que o segundo, deseja continuar mesmo assim? [1] Sim / [2] Não: "))
        if pergunta == 1:
            div = n1 / n2
            print(f"A subtração entre {n1} e {n2} é {div}")
        elif pergunta == 2:
            print("Finalizando...")
    elif n1 > n2:
        div = n1 / n2
        print(f"A subtração entre {n1} e {n2} é {div}")
    else:
        print(f"A subtração entre {n1} e {n2} é 0")

num1 = int(input("Digite um número: "))
num2 = int(input("DIgite outro: "))
menu()
ask = int(input("Digite sua opção: "))
if ask == 1:
    somar(num1, num2)
elif ask == 2:
    subtrair(num1, num2)
elif ask == 3:
    multiplicar(num1, num2)
elif ask == 4:
    dividir(num1, num2)
else:
    print("Opção inválida!")