idades = []

for i in range(6):
    valor = int(input('idade: '))
    idades.append(valor)

idades.sort(reverse=False)
print(idades)