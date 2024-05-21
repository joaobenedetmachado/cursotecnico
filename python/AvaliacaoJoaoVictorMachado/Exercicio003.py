# João Victor Benedet Machado - 1190

nome = str(input('Qual seu nome?: ')).lower().title()

print('/'*20)
print('PROEJETOS (P)'.center(20))
print('ENGENHARIA (E)'.center(20))
print('ADMINISTRATIVO (A)'.center(20))
print('COORDENADOR (C)'.center(20))
print('/'*20)

setor = str(input(f'Olá {nome}, escreva de que setor listado acima você é: ')).upper().strip()
salario = float(input('Escreva seu salário: '))

if setor == 'P':
    novosalario = (salario/100)*10 + salario
    print(f'{nome}, seu novo salário é de {novosalario} Reais.')
elif setor == 'E':
    novosalario = (salario/100)*8+ salario
    print(f'{nome}, seu novo salário é de {novosalario} Reais.')
elif setor == 'A':
    novosalario = (salario/100)*13 + salario
    print(f'{nome}, seu novo salário é de {novosalario} Reais.')
elif setor == 'C':
    novosalario = (salario/100)*5 + salario
    print(f'{nome}, seu novo salário é de {novosalario} Reais.')
else:
    print('CARGO NÃO ENCONTRADO NO SISTEMA.')


