lista1 = []
lista2 = []
lista3 = []

for i in range(3):
    num = int(input('digite o numero para o vetor 1: '))
    lista1.append(num)

for i in range(3):
    num = int(input('digite o numero para o vetor 2: '))
    lista2.append(num)


for i in range(0, 3):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(lista3)