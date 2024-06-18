dicLibs = {} # CRIEI O DICIONARIO

while True:
    print('--- MENU DE OPÇÕES ---')
    print('   1 - CADASTRAR')
    print('   2 - EXCLUIR')
    print('   3 - PESQUISAR')
    print('   4 - SAIR')

    escolha = int(input('>> '))

    if escolha == 1: # PERGUNTEI O NOME E O VALOR E ARMAZENEI NA DIC
        nomeLivro = input('NOME DO LIVRO >> ')
        valorLivro = int(input('VALOR >> '))
        dicLibs[nomeLivro] = valorLivro
        print(f' PEÇA {nomeLivro} COM {valorLivro} UNIDADES ADCIONADAS AO SISTEMA.')
    if escolha == 2: # PERGUNTEI O NOME, COM O POP EXCLUIU
        nomeLivro = input('NOME DO LIVRO >> ')
        dicLibs.pop(nomeLivro)
        print(f' PEÇA {nomeLivro} EXCLUIDA DO SISTEMA')
    if escolha == 3: # CRIEI UMA LISTA PARA ARMAZENAR O NOME DOS LIVROS E DPS COLOQUEI EM ORDEM, CRIEI A VARIEL COM A SOMA DE TODS OS VALUES E COM A QUANTIDADE
        nomeLivros = [] 
        for i in dicLibs.keys():
            nomeLivros.append(i)
        nomeLivros.sort(reverse=False)
        print("NOME DOS LIVROS EM ORDEM ALFABETICA: ")
        for i in nomeLivros:
            print(i)
        quantidadeTotalLivros = len(dicLibs.keys())
        quantidadeSomaLivros = sum(dicLibs.values()) 
        print(f' O SISTEMA TEM {quantidadeTotalLivros} LIVRO CADASTRADOS.')
        print(f' SOMA DE TODAS OS PRECOS {quantidadeSomaLivros}')
        for i,o in dicLibs.items():
            print(f"NOME: {i}, PREÇO: {o}")
    if escolha == 4: # aqui ele saiu do software, o break faria quase a mesma coisa
        print(' SAINDO DO PROGRAMA...')
        exit()