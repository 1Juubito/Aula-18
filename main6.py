nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
if nome == 'Allan':
    print('Bem vindo Allan')
elif idade < 18:
    print('Você é menor de idade')
elif idade > 100 :
    print('Você provavelmente é imortal')
