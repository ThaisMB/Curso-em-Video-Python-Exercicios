salário = float(input('Qual o salário do funcionário?'))

if salário <= 1500:

    novo = salário + salário*0.15

if salário > 1500:

    novo = salário + salário*10/100



print ('Quem ganhava R${:.2f} agora passará a ganhar R${:.2f}!'.format(salário, novo))
