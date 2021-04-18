from datetime import date
def voto(ano):
    idade=date.today().year-ano
    print(f'Com {idade} anos:', end='')
    if idade<16:
        print('NÃO VOTA')
    elif 18>idade>=16 or idade>65:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATÓRIO')


print('-'*60)
ano_nasc=int(input('Em que ano você nasceu?  '))
voto(ano_nasc)