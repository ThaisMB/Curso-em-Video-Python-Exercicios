from datetime import date
cadastro = dict()

cadastro['nome']=str(input('Nome:'))
nasc=int(input('Ano de Nascimento:'))
cadastro['idade']=(date.today().year-nasc)
cadastro['ctps']=int(input('Carteira de Trabalho(0 se não tem):'))
if cadastro['ctps']!=0:
    cadastro['contratação']=int(input('Ano de Contratação:'))
    cadastro['salário']=float(input('Salário: R$'))
    cadastro['aposentadoria']=cadastro['idade']+((cadastro['contratação']+35)-date.today().year)
print(cadastro)
print('-=-'*30)
for k,v in cadastro.items():
    print(f'- {k} tem o valor {v}')