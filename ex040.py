nota1= float(input('Primeira nota:'))
nota2= float(input('Segunda nota:'))
média= (nota1+nota2)/2

print('Tirando {} e {}, a média do aluno é de {}.'.format(nota1, nota2, média))

if média>7.0:
    print ('\33[34m O aluno está APROVADO!')

elif 7.0>média>=5.0:
    print('\33[33m O aluno está em RECUPERAÇÃOI!')

else:
    print('\33[31m O aluno está REPROVADO!')