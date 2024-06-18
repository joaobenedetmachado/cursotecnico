dicPecas = {}

while True:
    print('--- MENU DE OPÇÕES ---')
    print('   1 - CADASTRAR')
    print('   2 - EXCLUIR')
    print('   3 - PESQUISAR')
    print('   4 - SAIR')

    escolha = int(input('>> '))

    if escolha == 1:
        nomePeca = input('NOME DA PEÇA >> ')
        quantidadePeca = int(input('QUANTIDADE >> '))
        dicPecas[nomePeca] = quantidadePeca
        print(f' PEÇA {nomePeca} COM {quantidadePeca} UNIDADES ADCIONADAS AO SISTEMA.')
    if escolha == 2:
        nomePeca = input('NOME DA PEÇA >> ')
        dicPecas.pop(nomePeca)
        print(f' PEÇA {nomePeca} EXCLUIDA DO SISTEMA')
    if escolha == 3:
        quantidadeTotalPecas = len(dicPecas.keys())
        quantidadeMaiorPecas = max(dicPecas.values())
        quantidadeMenorPecas = min(dicPecas.values())
        quantidadeSomaPecas = sum(dicPecas.values())
        print(f' O SISTEMA TEM {quantidadeTotalPecas} PEÇAS CADASTRADAS.')
        print(f' MAIOR NUMERO DE PECAS {quantidadeMaiorPecas}')
        print(f' MENOR NUMERO DE PECAS {quantidadeMenorPecas}')
        print(f' SOMA DE TODAS AS QUANTIDADE {quantidadeSomaPecas}')
        print(' PECAS CADASTRADAS:')
        for keys, values in dicPecas.items():
            print(f'   item: {keys}, quant: {values}')
    if escolha == 4:
        print(' SAINDO DO PROGRAMA...')
        exit()