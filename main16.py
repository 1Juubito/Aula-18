while True:
    nome = input('Qual seu nome?')
    if (nome != 'Lenhadorzinho'):
        continue # volta para o inicio
    senha = input('Digite sua senha: ')
    if (senha == 'Uninter'):
        break #Encerra o laço
print('Acesso concedido!')