import random
numeros = []
qtd_numeros_sorteados = 0
n=0
print('-' * 30)
print('JOGA NA MEGASENA')
print('-' * 30)

qtd_jogos = (int(input('Quantos jogos você quer que eu sorteie?')))
print(f'Sorteando {qtd_jogos} jogos')

for c in range(1, qtd_jogos + 1):
    while qtd_numeros_sorteados < 6:
        n = random.randint(1,60)
        if n not in numeros:
            numeros.append(n)
            qtd_numeros_sorteados += 1
    
    qtd_numeros_sorteados = 0
    print(f'Jogo {c}: {numeros}')
    numeros.clear()