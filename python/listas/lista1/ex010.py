lista = []

for i in range(0, 3):
    valor = input('digite um valor: ')
    lista.append(valor)

lista.sort(reverse=True)
print(lista)