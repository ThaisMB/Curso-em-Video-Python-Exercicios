def fatorial(n, show=False):
    """fatorial(n,show=False):
      Calcula o fatorial de um número inteiro

    Args:
        n (int): recebe o número do qual se quer o fatorial
        show (bool, optional): mostra o processo

    Returns:
        f: resultado do fatorial de n
    """
    f=1
    for c in  range(n,0,-1):
        if show:
            if (c > 1):
                print(f' {c} ', end='x')
            else:
                print(f' {c} ', end='= ')
        f*=c
    return f

           
   


print(fatorial(4, True))

