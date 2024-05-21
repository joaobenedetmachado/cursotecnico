nome = str(input('qual seu nome: '))
print('SC - Santa Catarina')
print('PR - Parana')
print('RS - Rio Grande do Sul')
curso = str(input('Escolha o seu estado: ')).upper().split()

if curso == 'SC':
    print(f'{nome}, santa catarina')
elif curso == 'PR':
    print(f'{nome}, parana')
elif curso == 'RS':
    print(f'{nome}, rio grande do sul')  