nome = input('digite seu nome: ')
while True:
    senha = input('digite sua senha: ')
    if senha == nome:
        print('erro. senha = nome, refaça')
        continue
    else:
        print('salvo!')
        break