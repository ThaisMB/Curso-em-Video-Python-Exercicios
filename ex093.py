ficha=dict()
stotal=0
npartidas=0
gols=[]

ficha['nome']=str(input('Nome do jogador:'))
npartidas=int(input(f'Quantas partidas {ficha["nome"]} jogou?'))
for c in range(0,npartidas):
    g=(int(input(f'Quantos gols na partida {c}?')))
    gols.append(g)
    stotal=stotal+g
ficha['gols']=gols
ficha['total']=stotal
print('-='*30)
print(ficha)
print('-='*30)

for k,v in ficha.items():
    print(f'O campo {k} tem valor {v}.')


print('-='*30)
print(f'O jogador{ficha["nome"]} jogou {npartidas} partidas.')
for i,v in enumerate(gols):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {stotal} gols.')
