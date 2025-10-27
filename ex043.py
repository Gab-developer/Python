peso = float(input('Qual seu peso? (KG) '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura * altura)
print('Seu IMC é de {:.1F}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO do peso!')
elif 18.5 <= imc < 25:
    print('Peso IDEAL!')
elif 25 <= imc < 30:
    print('ACIMA do peso!')
elif 30 <= imc < 40:
    print('\033[0;31mOBESIDADE!!\033[m')
else:
    print('\033[0;30;41mOBESIDADE MÓRBIDA!!!\033[m')
