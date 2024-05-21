# João Victor Benedet Machado - 1190

nome = str(input('Digite seu nome: ')).lower().title()
pao = str(input(f'''Olá {nome}, que tipo de pão você comprou?
        
                SONHO (SO)
                CROISSANT (CR)
                PÃO FRANCES (PF)
                BAGUETE (BA)
                
                ''')).upper().strip()
quantidade = int(input('E qual a quantidade? '))

if pao == 'SO':
    print(f'O Valor é de R${quantidade * 3.50}')
elif pao == 'CR':
    print(f'O Valor é de R${quantidade * 2.50}')
elif pao == 'PF':
    print(f'O Valor é de R${quantidade * 3.00}')
elif pao == 'BA':
    print(f'O Valor é de R${quantidade * 4.00}')
else:
    print('produto ou valor nao indentificado no sistema.')