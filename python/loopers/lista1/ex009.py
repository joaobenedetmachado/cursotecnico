nome = input('escreva seu nome: ')
while True:
    numero = int(input('escreva sua nota: '))
    if numero > 10 or numero < 0:
        print('erro, digite novamente: ')
        continue
    else:
        print('ok!')
        break
    