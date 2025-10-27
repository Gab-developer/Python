cont = -1
n1 = 0
soma = 0
while True:
    n1 = int(input('Digite um número [digite 999 para parar]: '))
    cont += 1
    soma += n1
    if n1 == 999:
        print('Você digitou {} números e a soma deles é de {}!'.format(cont, soma - 999))
        break