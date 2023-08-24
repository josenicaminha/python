n=str(input('Digite o nome do aluno:   '))
n1=float(input('Digite a primeira nota do aluno:  '))
n2=float(input('Digite a segunda nota do aluno:  '))
n3=float(input('Digite a terceira nota do aluno'))
if(n1>=6.0 and n2>=6.0 and n3>=6.0):
    m = (n1 + n2 + n3)/3
    print('Como o aluno {} obteve {} na primeira nota, {} na segunda e {} na terceira, ele ficou com a média: {}'.format(n, n1, n2, n3,
                                                                                                          m))
else:
    rp = float(input('Digite a nota de recuperação paralela'))
    m=(n1+n2+n3+rp)/4
    print('Como o aluno {} obteve {} na primeira nota, {} na segunda , {} na terceira e {} na recuperação paralela, ele ficou com a média: {}'.format(n,n1,n2,n3,rp,m))





