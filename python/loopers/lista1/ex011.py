while True:
    nome = input('escreva seu nome: ')
    if len(nome) < 3:
        print('nome menor que 3 caracteres: refaça')
        continue
    else:
        while True:
            salario = int(input('escreva seu salario: '))
            if salario < 0:
                print('valor menor que zero, refaça')
                continue
            else:
                while True:
                    estadocivil = input('escreva seu estado civil (S)olteiro ou (C)asado: ').upper()
                    if estadocivil == 'S' or estadocivil == "C":
                        while True:
                            idade = int(input('escreva sua idade: '))
                            if idade < 0 or idade > 100:
                                print('idade nao esta entre 0 - 100 anos, refaça')
                                continue
                            else:
                                while True:
                                    sexo = input('escreva seu sexo: ').upper()
                                    if sexo == 'F' or sexo == "M":
                                        print('castrado.')
                                        exit()                                  
                                    else:
                                        print('Diferente de M ou F, tente novamente')
                                        continue
                    else:
                        print('Diferente de C ou S, tente novamente')
                        continue
                        
