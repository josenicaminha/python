n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota:  '))
m=(n1+n2)/2
print('A média do aluno foi:{:.1f}'.format(m))
if m>=6:
    print('O aluno foi aprovado')
else:
    print('O aluno está reprovado')
    print('__F I M __')
