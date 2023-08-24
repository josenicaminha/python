n=str(input('Diga o seu nome:     '))
v=float(input('Informe o valor do imóvel que você deseja comprar:'))
s=float(input('Agora me informe qual é o seu salário:'))
f=int(input('Diga em quantos anos voê deseja pagar:'))
prestação=v/f
if prestação>0.3*s:
    print('Desculpe-me Sr(a).\033[1;32;41m {}\033[m, mas infelizmente o empréstimo não foi aprovado.'.format(n))
else:
    print('\033[1;34;41m PARABÉNS Sr(a). {}!!!!\033[m Seu empréstimo foi aprovado.'.format(n))

