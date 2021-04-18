pessoas= []
dados = []
maiorp=menorp=0
maisp=[]
menosp=[]
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    
    if len(pessoas)==0:
        maiorp=menorp=dados[1]
    else:
        if dados[1]>maiorp:
            maiorp=dados[1]
        elif dados[1]<menorp:
            menorp=dados[1]
    pessoas.append(dados[:]) 
    dados.clear()
        
    resposta=str(input('Deseja continuar?[S/N]')).upper()
    if resposta=='N':
        break
for d in pessoas:
    if d[1]==maiorp:
        maisp.append(d[0])

    if d[1]==menorp:
        menosp.append(d[0])
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'Os dados foram {pessoas}')   

print(f'O maior peso foi de {maiorp}. Peso de {maisp}.')
print(f'O menor peso foi de {menorp}. Peso de {menosp}.')