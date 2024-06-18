nomeslista = [] #criei as listas que seriam utilizadas posteriormente
salarioslista = []

while True: #Iniciei o ciclo para que isso ocorra até que haja um break ou exit()
    print("---|| MENU DE OPÇOES ||---")
    print("   1 - Cadastrar   ")
    print("   2 - Excluir   ")
    print("   3 - Exibir   ")
    print("   4 - Sair   ")

    escolha = int(input(">> "))

    if escolha == 1: 
        nome = input('DIGITE O NOME: ')
        salario = float(input('DIGITE O SALARIO: '))
        nomeslista.append(nome)
        salarioslista.append(salario)
        print(f'USUARIO {nome} DE SALARIO {salario} ADCIONADOS AO SISTEMA') #  
    if escolha == 2: 
        nome = input('DIGITE O NOME: ')
        salario = float(input('DIGITE O SALARIO: '))
        nomeslista.remove(nome)
        salarioslista.remove(salario)
        print(f'USUARIO {nome} DE SALARIO {salario} REMOVIDOS DO SISTEMA') 
    if escolha == 3:  
        maiorsalario = max(salarioslista) 
        menorsalario = min(salarioslista) 
        somasalarios = sum(salarioslista) 
        quantidadeusuarios = len(nomeslista) 
        nomeslista.sort(reverse=False) 
        print('USUARIOS CADASTRADOS:')
        for i in nomeslista: #Joao, kaike, lucas, mateus, davi
            print('  ',i)
        # 
        print(f'MAIOR SALARIO {maiorsalario}')
        print(f'MENOR SALARIO {menorsalario}')
        print(f'SOMA DE TODOS OS SALARIOS: {somasalarios}')
        print(f'QUANTIDADE DE USUARIOS: {quantidadeusuarios}')
    if escolha == 4: #sai do programa (o mesmo funcionaria com o break, por exemplo)
        print('SAINDO DO PROGRAMA...')
        exit()