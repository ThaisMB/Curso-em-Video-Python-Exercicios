mvelho = ('Nome')
ivelho = 0
m20 = 0
soma = 0
média = 0


for c in range(1,5):

    print('----- {}º pessoa -----'.format(c))
    nome = input('Nome:')
    idade =int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper()
    soma = soma + idade

    if sexo == 'M' and idade> ivelho:

        ivelho = idade
        mvelho = nome

    elif sexo == 'F' and idade<20:

        m20 = m20+1

média =int( soma/c)

print('A média de idade do grupo é de {} anos.'.format(média))
print('O homem mais velho tem {} anos e se chama {}.'.format(ivelho, mvelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(m20))