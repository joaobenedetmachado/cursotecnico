fanta = 0
sprit = 0
cocacola = 0
count = 0
while count < 300:
    nome = input('qual seu nome? ')
    cidade = input('de que area voce é: ').lower()
    if cidade == 'fanta':
        fanta = fanta + 1
    elif cidade == 'sprit':
        sprit = sprit + 1
    elif cidade == 'cocacola':
        cocacola = cocacola + 1
    count = count + 1

print(fanta, sprit, cocacola)