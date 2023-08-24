n=int(input('Digite um número inteiro: '))
b=int(input('Agoar escolha a base que você quera que eu converta. 1-Binário, 2-Octal e 3-Hexadecimal'))
def convert_to_bin(numero):
    return bin(numero)[2:]
def convert_to_hex(numero):
    return hex(numero)[2:]
def convert_to_oct(numero):
    return oct(numero)[2:]
if b==1:
    print('O valor de {} na base 2 é igual a {}'.format(n,convert_to_bin(n)))
elif b==2:
    print('O valor de {} na base octal é igual a {}'.format(n,convert_to_oct(n)))
elif b==3:
    print('O valor de {} na bae hexadecimal é igual a {}'. format(n,convert_to_hex(n)))
