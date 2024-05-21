reprovados = aprovados = count = 0

while count < 10:
    nome = input('qual seu nome: ')
    media = int(input('sua media final: '))
    if media < 7:
        reprovados += 1
    elif media >= 7:
        aprovados += 1
    count += 1
    
print(aprovados, reprovados)