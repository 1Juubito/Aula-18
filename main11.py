kWh = float(input('Qual a quantidade de Kwh consumida? '))
tipo = input('Qual o tipo de instalação? (R/I/C) ').upper()

if tipo == "R":
    if kWh >= 500:
        preco = 0.65
    else:
        preco = 0.4
    print(f'O valor a pagar é de {kWh * preco}')
elif tipo == "I": 
    if kWh >= 1000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'O valor total a pagar é de {kWh * preco}')
elif tipo == "C":
    if kWh >= 5000:
        preco = 0.6
    else:
        preco = 0.55
    print(f'O Valor a pagar é de {kWh * preco}')
else:
    print('Instalação inválida!')