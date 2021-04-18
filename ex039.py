from datetime import date

ano = int(input('Ano de Nascimento:'))

aatual = date.today().year

idade = aatual-ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, aatual))

if idade<18:
    tempo= 18-idade
    aal= aatual+tempo

    print('Ainda faltam {} anos para o alistamento.'.format(tempo))
    print('Seu alistamento será em {}.'.format(aal))

elif idade>18:
    tempo= idade-18
    aal=aatual-tempo

    print('Você já deveria ter se alistado há {} anos.'.format(tempo))
    print('Seu alistamento foi em {}.'.format(aal))

else:
    print('Você tem que se alistar IMEDIATAMENTE!')