print('V - VENDAS')
print('C - COMPRAS')
print('P - PRODUÇÃO')
escolha = str(input('escreva seu cargo na empresa: '))
salario = float(input('escreva seu salario atual: ')).upper().split()

if escolha == 'V':
    print('seu novo salario é', (salario/100)*10 + salario)
elif escolha == 'C':
    print('seu novo salario é', (salario/100)*8 + salario)
else:
    print('seu novo salario é', (salario/100)*15 + salario)