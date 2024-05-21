notas = []

for i in range(3):
    valor = int(input('digite sua nota '))
    notas.append(valor)

media = (sum(notas))/len(notas)
print(media)