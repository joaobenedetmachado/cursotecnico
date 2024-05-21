media = []

for i in range(5):
    nota1 = int(input('nota1: '))
    nota2 = int(input('nota2: '))
    nota3 = int(input('nota3: '))
    mediaind = (nota1 + nota2 + nota3) / 3 
    media.append(mediaind)
    print(mediaind)

for i in media:
    if i >= 7:
        print(i)
