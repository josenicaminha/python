s=0
for c in range(1,500,2):
    print(c)
    n=c
    s+=n
print('O somatório de todos os números ímpares de 1 até 500 é:\033[1;30;41m {}\033[m'.format(s))
