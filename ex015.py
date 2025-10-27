d = int(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos KM rodados? '))
valord = d * 60
valorkm = km * 0.15
soma = valord + valorkm
print('De acordo com {} dias alugados e {}Km rodados, podemos dizer que o total a pagar será de {}'.format(d, km, soma))
