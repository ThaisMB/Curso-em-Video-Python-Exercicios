dados=dict()
grupo=list()
opc='0'
sidade=0
grupomulheres=list()

while True:
    dados=dict()
    nome=str(input('Nome:'))
    dados['nome']=nome
    sexo=str(input('Sexo:'))
    while sexo not in 'MmFf':
        print('ERRO! Por favor, digite apenas F ou M.') 
        sexo = str(input('Sexo:'))
    dados['sexo']=sexo
    if sexo in 'Ff':
        grupomulheres.append(nome)
    idade=int(input('Idade:'))
    dados['idade']=idade
    sidade+=idade
    grupo.append(dados)
    while opc not  in 'NnSs':
        opc=str(input('Quer continuar? [S / N]'))
        if opc not in 'NnSs':
            print('ERRO! Responda S ou N.')
    if opc in 'Nn':
            break
    else:
        opc='0'
print('-='*36)
print(f'A)Ao todo temos {len(grupo)} pessoas cadastradas')

media=sidade/len(grupo)
print(f'B)A média de idade é de {media :2} anos.')

print(f'C)As mulheres cadastradas foram ', end=' ')
for v in grupomulheres:
    print(v,end=' ')
print()

print(f'D)As pessoas com idade acima da média foram:')

for pessoa in grupo:
    if pessoa["idade"] > media:
        for k, v in pessoa.items():
            print(f"{k}= {v}", end=' ')
