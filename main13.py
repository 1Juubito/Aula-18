soma = 0
cont = 1
while (cont <= 5):
    x = float(input(f'Digite a {cont}ª nota: '))
    soma += x #equivalente: soma + x
    cont += 1 #equivalente: cont + 1
media = soma / 5
print(f'Média final: {media}')