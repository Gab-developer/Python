dis = int(input('Digite a distancia da sua viagem (Em Km): '))
print('Você está prestes a comçar uma viagem de {} Km!'.format(dis))
if dis <= 200:
    preco = dis * 0.50
    print('O preço da viagem é de R${}'.format(preco))
else:
    ter = dis *0.45
    print('O preço da viagem é de R${}'.format(ter))
print('Tenha uma boa viagem!')
