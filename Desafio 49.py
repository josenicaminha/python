n1=int(input('Digite um numero de 1 a 9 que você queira ver a tabuada do mesmo: '))
for c in range(0,11):
    print('{} x {} = '.format(n1,c))
    print(c*n1)
print('\033[2;30;45m F I M \033[m')