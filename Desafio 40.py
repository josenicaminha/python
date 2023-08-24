import math
n1=float(input('Digite a primeira nota:  '))
n2=float(input('Digite a segunda nota:  '))
n3=float(input('Digite a terceira nota:  '))
média=(n1+n2+n3)/3
if math.floor(média)<5.0:
    print('\033[0;30;41m Lamentavelmente você foi reprovado.\033[m, pois a sua média foi {}'.format(math.floor(média)))
elif math.floor(média)>=5.0 and math.floor(média)<=5.9:
    print('\033[0;43m Você deve estudar mais um pouco, pois ficou de recuperação.\033[m,pois a sua média foi {}'.format(math.floor(média)))
elif math.floor(média)>=7.0:
    print('\033[0;30;42m PARABÉNS!!!!! Você foi aprovado.\033[m,pois a sua média foi {}'.format(math.floor(média)))