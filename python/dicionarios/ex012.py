dic = {"Arroz": 5.35, "Cafe": 1.99, "Leite": 4.99}


while True :

    print("---   MENU   ---")
    print("1 - cadastrar ")
    print("2 - pesquisar")
    print("3 - alterar")
    print("4 - excluir")
    print("5 - incluir novo produto")
    print("6 - sair")

    escolha = int(input("> "))

    if escolha == 1:
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preco do produto: "))
        dic[produto] = preco

    if escolha == 2:
        prodmaiscaro = max(dic.values())
        prodmaisbarato = min(dic.values())
        quantidade = len(dic.items())
        soma = sum(dic.values())
        print("Produto mais caro: ", prodmaiscaro)
        print("Produto mais barato: ", prodmaisbarato)
        print("Quantidade: ", quantidade)
        print("Soma: ", soma)
        produto = input("Digite o nome do produto: ")
        print(f'{produto} : {dic.get(produto, 'nao encontrado')}')
    
    if escolha == 3:
        produto = input("Digite o nome do produto: ")
        if produto in dic.keys():
            print('produto existente')
            preco = float(input("Digite o preco do produto: "))
            dic.update({produto : preco})
        else:
            print("inexistente")

    if escolha == 4:
        produto = input("Digite o nome do produto: ")
        dic.pop(produto)

    if escolha == 5: 
        produto = input("Digite o nome do produto: ")
        preco = float(input("Digite o preco do produto: "))
        dic[produto] = preco

    if escolha == 6:
        exit()

    print(dic)
        

