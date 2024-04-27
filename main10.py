palavra = '|CALCULADORA|'
print('-'*len(palavra))
print(palavra)
print('-'*len(palavra))

print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Pressione qualquer tecla para sair.')

op = input('Qual operação deseja? ')
v1 = int(input('Digite um número inteiro: '))
v2 = int(input('Digite outro número inteiro: '))

if op == ('+'):
    print(f'O valor de {v1} + {v2} é = {v1 + v2} ')
elif op == ('-'):
    print(f'O valor de {v1} - {v2} é = {v1 - v2} ')
elif op == ('*'):
    print(f'O valor de {v1} x {v2} é = {v1 * v2} ')
elif op == ('/'):
    print(f'O valor de {v1} / {v2} é = {v1 / v2} ')
else:
    print('Encerrando o programa...')