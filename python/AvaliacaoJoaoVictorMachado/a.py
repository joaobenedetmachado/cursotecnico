listaprodutos = [] # criei as listas que eu utilizarei depois
listaprecos = []

while True: #iniciei o laco while true, para que pare quando houver um exit() ou break
    print("---|| MENU DE OPÇOES ||---")
    print("   1 - Cadastrar   ")
    print("   2 - Excluir   ")
    print("   3 - Exibir   ")
    print("   4 - Sair   ")

    escolha = int(input(">> "))

    if escolha == 1:#perguntei o nome do produto junto com seu preco, ambas as variaveis seriam adicionadas as suas respectivas listas
        produto = input('DIGITE O NOME DO PRODUTO: ')
        preco = float(input('DIGITE O PRECO DO PRODUTO: '))
        listaprodutos.append(produto)
        listaprecos.append(preco)
        print(f'PRODUTO {produto} DE PRECO {preco} CADASTRADOS AO SISTEMA')
    if escolha == 2:#perguntei o nome do produto junto de seu preco, e com o .remove(), seria excluido de suas respectivas listas
        produto = input('DIGITE O NOME DO PRODUTO: ')
        preco = float(input('DIGITE O PRECO DO PRODUTO: '))
        listaprodutos.remove(produto)
        listaprecos.remove(preco)
        print(f'PRODUTO {produto} DE PRECO {preco} EXCLUIDOS DO SISTEMA')
    if escolha == 3:
        menorpreco = min(listaprecos) #criei a variavel do menor preco que sera medida com o min()
        maiorpreco = max(listaprecos) #criei a variavel do maior preco que usara o max()
        quantidadeprodutos = len(listaprodutos) #criei mais uma para eu saber a quantidade de elementos da lista com o len()
        listaprodutos.sort(reverse=False) #lista dos produtos em ordem albetica por conta do reverse=False
        listaprecos.sort(reverse=False) #lista dos precos em ordem crescente por conta do reverse=False
        maiorque100 = 0 #variavel de controle 
        print('PRODUTOS CADASTRADOS: ')
        for i in listaprodutos: #exibe os produtos com um print para cada
            print('  ',i)
        print('PRECOS CADASTRADOS: ') #aqui faz a mesma coisa porem caso o preco for maior que 100, ele ira adicionar + 1 na variavel de controle
        for i in listaprecos:
            print('  ', i)
            if i > 100:
                maiorque100 = maiorque100 + 1
        print(f'QUANTIDADE DE PRECOS MAIOR QUE 100: {maiorque100}')
        print(f'QUANTIDADE DE PRODUTOS: {quantidadeprodutos}')
    if escolha == 4: #caso selecionado opcao 4, sai do programa com o exit (o break funcionaria tambem)
        print('SAINDO DO PROGRAMA...')
        exit()
