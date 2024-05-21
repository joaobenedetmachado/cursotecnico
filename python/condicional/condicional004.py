mediaFinal = float(input('escreva sua media final: '))

if mediaFinal >= 7:
    print('aprovado')
elif mediaFinal <7 and mediaFinal >= 5:
    print('recuperacao')
elif mediaFinal <5:
    print('reprovado')