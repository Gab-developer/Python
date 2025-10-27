n1 = soma = 0
cont = -1
while n1 != 999:
    n1 = int(input('Digite um número [digite 999 para parar]: '))
    soma += n1
    cont += 1
print('Você digitou {} números e a soma deles é de {}'.format(cont, soma - 999))