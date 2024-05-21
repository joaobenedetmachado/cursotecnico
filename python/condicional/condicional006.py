nome = str(input('qual seu nome: '))
print('D - Divorciado')
print('C - Casado')
print('S - Solteiro')
print('V - Viuvo')
curso = str(input('Escolha o seu estado civil: '))

if curso == 'D':
    print(f'{nome}, divorciado')
elif curso == 'C':
    print(f'{nome}, casado')
elif curso == 'S':
    print(f'{nome}, solteiro')
elif curso == 'V':
    print(f'{nome}, viuvo')   