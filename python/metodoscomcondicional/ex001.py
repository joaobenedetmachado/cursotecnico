nome = str(input('qual seu nome: '))
print('ADM - Administração')
print('DIR - Direito')
print('COM - Comercio')
curso = str(input('Escolha o curso: ')).upper().split()

if curso == 'ADM':
    print(f'{nome}, curso Administração')
elif curso == 'DIR':
    print(f'{nome}, curso Direito')
elif curso == 'COM':
    print(f'{nome}, curso Comercio')
    
 