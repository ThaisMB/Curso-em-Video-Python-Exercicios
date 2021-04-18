teste = list()
teste.append('Gustavo')
teste.append(40)
print(teste)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 19

galera.append(teste[:])

print(teste)
print(galera)

galera = [['João',22], ['Flora',12], ['Jurema', 25], ['Tiana', 34]]

print(galera[0])

print(galera[2][1])

for p in galera:
    print(f'{(p[0])} tem {p[1]} anos de idade.')

