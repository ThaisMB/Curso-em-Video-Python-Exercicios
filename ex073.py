times = ('São Paulo','Atlético-MG', 'Flamengo', 'Palmeiras','Internacional', 'Grêmio', 'Fluminense', 'Santos', 'Corinthians','Ceará SC', 'Bragantino', 'Atlético-GO', 'Fortaleza', 'Athlético-PR','sport Recife', 'Bahia', 'Vasco da Gama', 'Coritiba', 'Goiás','Botafogo')

print('-=-'*40)
print(f'Lista de Times do Brasileirão:{times}')

print('-=-'*40)
print(f'Os 5 primeiros são:{times[:5]}')

print('-=-'*40)
print(f'Os 4 últimos são:{times[-4:]}')

print('-=-'*40)
print(f'Os times em ordem alfabética são:{sorted(times)}')

print('-=-'*40)

if 'Chapecoense' in times:
    print('O Chapecoense está na {}ª posição.'.format(times.index('Chapecoense')))
else:
    print('O Chapecoense não está entre os times do Brasileirão nessa temporada.')

print('-=-'*40)

