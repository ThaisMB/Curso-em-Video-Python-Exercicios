def notas(*n, sit=False):
    """notas(*n, sit=False) -> Funcao para analisar notas e situacoes de alunos.

    Args:
        n(float):uma ou mais notas de alunos(aceita varias)
        sit (bool, optional): indica se a situacao deve ou nao ser adicionada. Defaults to False.

    Returns:
        aluno: dicionario com o total de notas, a maior nota, a menor nota, a media e, caso opte, 
        a situacao do aluno/turma.
    """
    aluno=dict()
    aluno['total']=len(n)
    aluno['maior']=max(n)
    aluno['menor']=min(n)
    aluno['média']=sum(n)/len(n)
    if sit:
        if aluno['média']<5:
            aluno['situação']='RUIM'
        elif 7>aluno['média']>=5:
            aluno['situação']='RAZOÁVEL'
        elif aluno['média']>=7:
            aluno['situação']='BOA'
    return aluno


r=notas( 6.5, 2.5,1.0, sit=True)
print(r)
help(notas)