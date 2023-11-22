import random 
##biblioteca utilizada para randomizar os numers


input(print('Digite J para jogar o dado:'))
##apenas uma interacao com o usuario


numero = random.randint(1,6)
##declarando a variavel numero ja com o modulo random trabalhando dentro dela


if numero == 1:
    print('Numero {0}'.format(numero))
    print   ('00000')
    print   ('00x00')
    print   ('00000')
elif numero == 2:
    print('Numero {0}'.format(numero))
    print   ('000x0')
    print   ('00000')
    print   ('0x000')
elif numero == 3:
    print('Numero {0}'.format(numero))
    print   ('000x0')
    print   ('00x00')
    print   ('0x000')
elif numero == 4:
    print('Numero {0}'.format(numero))
    print   ('0x0x0')
    print   ('00000')
    print   ('0x0x0')
elif numero == 5:
    print('Numero {0}'.format(numero))
    print   ('0x0x0')
    print   ('00x00')
    print   ('0x0x0')
else:
    print('Numero {0}'.format(numero))
    print   ('0x0x0')
    print   ('0x0x0')
    print   ('0x0x0')

