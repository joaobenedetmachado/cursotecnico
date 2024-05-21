par = []
impar = []

for i in range(6):
    valor = int(input('digite o numero: '))
    if (valor % 2) == 0:
        par.append(valor)
        print('par')
    else:
        impar.append(valor)
        print('impar')

print(impar, par)