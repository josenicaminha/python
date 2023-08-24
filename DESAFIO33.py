#import math
#def menu():
 #   num1=int(input('Digite o primeiro número:  '))
  #  num2=int(input('Digite o segundo número:   '))
  #  num3=int(input('Digite o terceiro número:  '))
#def max(num1,num2,num3):
#max=num1
 #   if num2>max:
  #      max=num2
  #  if num3>max:
  #      max=num3
#return max

#def min(num1,num2,num3):
 #   min=num1
  #  if num2<min:
   #     min=num2
    #if num3<min:
     #   min=num3
    #return min

#while true:
 #   menu()
#print('o maior número é {} e o menor é o {}'.format(max,min))


def maior(x, y, z):
    max = x

    if y > max:
        max = y
    if z > max:
        max = z

    return max


def menor(x, y, z):
    min = x

    if y < min:
        min = y
    if z < min:
        min = z

    return min


def menu():
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero : '))
    z = int(input('Terceiro: numero: '))

    print("Maior: ", maior(x, y, z))
    print("Menor: ", menor(x, y, z))
    print()


while True:
    menu()

