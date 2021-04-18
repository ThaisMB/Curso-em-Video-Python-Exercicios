dias= float(input('Quantos dias alugado?'))
km=float(input('Quantos kms rodados?'))
total= (dias*60)+ (km*0.15)

print('O total a pagar pelo aluguel é R${:.2f}'.format(total))