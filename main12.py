kwh = float(input('Digite o kwh comsumido: '))
tipo = input('Digite o tipo de instalação: (R/I/C)').upper()

if tipo == "R":
    if kwh >= 500:
        preco = 0.65
    else:
        preco = 0.4
    print(f'Valor a pagar: {kwh * preco:.2f}')
elif tipo == "C":
    if kwh >= 1000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'Valor a pagar: {kwh * preco:.2f}')
elif tipo == "I":
    if kwh >= 5000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'Valor a pagar: {kwh * preco:.2f}')
else:
    print('Instalação inválida')