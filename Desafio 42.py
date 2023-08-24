import math
r1=int(input('Informe o tamanho da reta1:   '))
r2=int(input('Informe o tamanho da reta2:   '))
r3=int(input('Informe o tamanho da reta3:   '))
if (r1+r2)>r3 and (r2+r3)>r1 and (r1+r3)>r2:
    print('\033[3;30;45m Estas retas formam um triângulo\033[m')
    if (r1==r2 and r2==r3):
        print('\033[1;32;40m  EQUILÁTERO  \033[m')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('\033[3;33;40m ESCALENO \033[m')
    elif r1==r2 or r1==r3 or r2==r3:
        print('O triângulo formado é um \033[0;38;47m ISÓCELES\033[m')
elif (r1+r2)<=r3 or (r2+r3)<=r1 or (r1+r3)<=r2:
    print('\033[2;33;45m Estas retas não formam um triângulo\033[m')

