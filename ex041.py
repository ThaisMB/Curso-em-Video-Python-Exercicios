from datetime import date

anonasc=int( input('Ano de Nascimento:'))

aatual= date.today().year

idade = (aatual-anonasc)

print('O atleta tem {} anos.'.format(idade))

if idade>=25:
    print('Classificação: MASTER')

elif idade>=14:
    print('Classificação: SÊNIOR')

elif idade>=9:
    print('Classificação: INFANTIL')

else:
    print('Classificação: MIRIM')