while True:
    print('''
        1 - adicao
        2 - subtracao
        3 - multiplicação
        4 - divisão
        5 - saida
        ''')
    escolha = int(input('escolha: '))
    numero1 = int(input('primeira entrada: '))
    numero2 = int(input('segunda entrada: '))
    if escolha == 1:
        print(numero1 + numero2)
    elif escolha == 2:
        print(numero1 - numero2)
    elif escolha == 3:
        print(numero1 * numero2)
    elif escolha == 4:
        print(numero1 / numero2)
    elif escolha == 5:
        print('saiu.')
        exit()