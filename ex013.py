salario=float(input('Qual é o salário do funcionário?'))
aumento= salario+(salario*15/100)
print('Um funcionário que ganhava R${:.2f}, com aumento de 15%, passará a ganhar R${:.2f}.'.format(salario, aumento))