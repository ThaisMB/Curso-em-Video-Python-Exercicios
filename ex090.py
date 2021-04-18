turma=dict()

turma['nome']=str(input('Nome:'))
turma['média'] = float(input(f'Média de {turma["nome"]}:'))
if 5.0<turma['média']<7.0:
    turma['situação']='Recuperação'
elif turma['média']<5.0:
    turma['situação']='Reprovado'
else:
    turma['situação']='Aprovado'

print('-='*30)
for k, v in turma.items():
    print(f'- {k} é igual a {v}')
