vetor1 = []
vetor2 = []
vetor3 = []

for i in range(5):
    valor1 = int(input('valor 1: '))
    vetor1.append(valor1)

for i in range(5):
    valor2 = int(input('valor 2: '))
    vetor2.append(valor2)

for i in range(5):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print(vetor1)
print(vetor2)
print(vetor3)