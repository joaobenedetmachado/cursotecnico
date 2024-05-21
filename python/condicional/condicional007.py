idade = int(input('escreva sua idade: '))

if idade == 0 and idade <= 10:
    print('infantil')
elif idade >=11 and idade <= 17:
    print('juvenil')
elif idade >= 18 and idade <= 29:
    print('adulto')
elif idade >= 30 and idade <= 60:
    print('senior')
