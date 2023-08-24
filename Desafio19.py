import random
n1=input('Digite o nome do primeiro aluno:  ')
n2=input('Digite o nome do segundo aluno:  ')
n3=input('Digite o nome do terceiro aluno:  ')
n4=input('Digite o nome do quarto aluno:  ')
lista=[n1,n2,n3,n4]
sorteado=random.choice(lista)
print ('sorteio')
#print('O sorteado foi o aluno: {}'.format(sorteado))
print('O sorteado foi o aluno: ' + sorteado)
#print('o sorteado foi:    '+ lista[random.randrange(len(lista))])



