A = int(input('Digite o 1º lado do triângulo: '))
B = int(input('Digite o 2º lado do triângulo: '))
C = int(input('Digite o 3º lado do triângulo: '))

if ((A > 0 and B > 0 and C > 0) and (A + B > C and A+ C > B and B + C > A)):
    #Se chegou até aqui, é porque o triângulo é válido.
    if (A != B and A != C and B != C):
        print('Triângulo Escaleno!')
    elif (A == B and B == C):
        print('Triângulo Equilátero!')
    else:
        print('Triângulo Isósceles!')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')