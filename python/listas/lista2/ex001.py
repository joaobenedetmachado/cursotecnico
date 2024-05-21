lista = []

for i in range(5):
    valor = int(input("Insira um valor: "))
    lista.append(valor)

print(lista)
lista.sort(reverse=True)
print(lista)