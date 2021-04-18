casa = float(input('Valor da casa: R$'))
salc = float(input('Salário do comprador: R$'))
tempo = float(input('Quantos anos de financiamento?'))
prestação = casa/(tempo*12)
pmáxima = salc*(30/100)

print('Para pagar uma casa de R$ {:.2f} em {:.0f} anos a prestação será de R$ {:.2f}.'.format(casa, tempo, prestação))

if prestação < pmáxima:
    print('Empréstimo pode ser CONCEDIDO')

else:
    print('Empréstimo NEGADO!')
