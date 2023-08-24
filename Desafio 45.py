from random import randint
input('Vamos começar a jogar o jogo Pedra, Papel e Tesoura????')
r=int(input('Se você quer jogar comigo digite 1, caso contrário digite 2:  '))
if r==2:
   print('Não tem problema, jogaremos em outra oportunidade!')
elif r==1:
    print('Ótimo! Vamos começar então!!!')
    nome=input('Diga para mim qual é o seu nome?')
    escolha = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0,2)
    print('''Suas opções:)
    [0] Pedra
    [1] Papel
    [2] Tesoura''')
    jogador = int(input('Comece fazendo a sua jogada {}'.format(nome)))
    print('*_' * 11)
    print('jogador jogou {}'.format(escolha[jogador]))
    print('Computador jogou {}'.format(escolha[computador]))
    print('*_' * 11)
    if computador == jogador:
       print('\033[0;30;45m SAIU EMPATE!!!\033[m')
    elif computador == 1 and jogador == 0 or computador == 0 and jogador == 2 or computador == 2 and jogador == 1:
       print('\033[0;33;40m COMPUTADOR GANHOU!!!\033[m')
    elif computador == 0 and jogador == 1 or computador == 2 and jogador == 0 or computador == 1 and jogador == 2:
        print('\033[1;32;43m JOGADOR GANHOU DO COMPUTADOR\033[m')
    print('OBRIGADO POR TER JOGADO COMIGO \033[0;33;46m {}\033[m'.format(nome))



