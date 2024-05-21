print('*'*30)
print('CALCULADORA DE GRANDEZAS'.center(30))
print('*'*30)
print('1 Tensão (em Volt)')
print('2 Resistencia (em Ohm)')
print('3 Corrent (em Ampére)')
print('4 Saida =>')
print('*'*30)
while True:
    escolha = int(input('Qual deseja escolher: '))
    if escolha == 1:
        resistencia = int(input('valor da resistencia: '))
        corrente = int(input('valor da corrente: '))
        print(corrente*resistencia)
    elif escolha == 2:
        tensao = int(input('valor da tensao:'))
        corrente = int(input('valor da corrente: '))
        resistencia = tensao/corrente
    elif escolha == 3:
        tensao = int(input('valor da tensao:'))
        resistencia = int(input('valor da resistencia: '))
        corrente = tensao/resistencia
    elif escolha == 4:
        print('saiu.')
        exit()

