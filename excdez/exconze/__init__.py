def resumo(n=0, a=0, d=0):
    metade= n/2
    dobro=n*2
    aumenta=n+(n*a/100)
    diminui= n-(n*d/100)

    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)
    print(f'Preço analisado:\t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(dobro)}')
    print(f'Metade do preço:\t{moeda(metade)}')
    print(f'{a}% de aumento:\t\t{moeda(aumenta)}')
    print(f'{d}% de redução:\t\t{moeda(diminui)}')
    print('-'*40)
def moeda(n=0, moeda='R$'):
    res= (f'{moeda}{n:>10.2f}'.replace('.',','))
    return res

def leiaDinheiro(msg):
    válido=False
    while not válido:
        entrada=str(input(msg)).replace(',','.')
        if entrada.strip().isalpha() or entrada.strip()=='':
            print(f'\033[31mERRO!"{entrada}"NÃO é um preço inválido!\033[m')
            
        else:
            válido=True
            return float(entrada)