base = 0
profissional = 0
veterano = 0
count = 0
while count < 100:
    resposta = int(input('digite seu resposta: '))
    if resposta >= 13 and resposta < 17:
        base = base +1
    if resposta >= 18 and resposta < 40:
        profissional = profissional +1
    if resposta >= 40:
        veterano = veterano +1
    count = count + 1
print(base, profissional, veterano)