idade = int(input('escreva sua idade: '))

if idade == 0 and idade <= 3:
    print('bebe')
elif idade >=4 and idade <= 11:
    print('criança')
elif idade >= 12 and idade <= 17:
    print('adolescente')
elif idade >= 18 and idade <= 60:
    print('adulto')
elif idade >= 61:
    print('idoso')