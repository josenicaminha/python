import math
r1=int(input('Informe o tamanho da primeira reta:'))
r2=int(input('Informe o tamanho da segunda reta:'))
r3=int(input('Informe o tamanho da terceira reta:'))
a=str('Essas retas formam um triângulo.')
b=str('Essas retas não formam um triângulo.')
if (r1+r2)>r3 and (r3+r2)>r1 and (r1+r3)>r2:
    print('De acordo com os dados que você forneceu \033[0;33;40m{}\033[m!!!'.format(a))
elif (r1+r2)<=r3 or (r2+r3)<=r1:
    print('De acordo com os dados que você forneceu \033[0;30;43m{}\033[m!!!'.format(b))
