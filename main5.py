palavra = '|Loja de Frutas|'
print('-'*len(palavra))
print(palavra)
print('-'*len(palavra))

print('1- Maçã')
print('2- Laranja')
print('3- Banana')

produto = int(input('Digite o produto desejado: '))
qtd = int(input('Digite a quantidade do produto desejado: '))

if (produto == 1):
    pagar = qtd * 2.30
    print(f'Você comprou {qtd} de maçãs. O valor total é de: {pagar:.2f}')
elif (produto == 2):
    pagar = qtd * 3.60
    print(f'Você comprou {qtd} laranjas. O valor total é de: {pagar:.2f}')
elif (produto == 3):
    pagar = qtd * 1.85
    print(f'Você comprou {qtd} bananas. O valor total é de: {pagar:.2f}')
else:
    print('Produto inválido!')
print('Fim do Programa!')