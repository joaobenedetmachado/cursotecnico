lista = []

for i in range(5):
    valor = int(input('digite um valor: '))
    lista.append(valor)

maior = max(lista)
menor = min(lista)
print(maior, menor)