notas = []

for i in range(5):
    nota1 = int(input('1 nota: '))
    nota2 = int(input('2 nota: '))
    notas.append((nota1 + nota2) / 2)
    print((nota1 + nota2) / 2)

print(notas)