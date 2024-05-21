flamengo = 0
vasco = 0
cocacola = 0
count = 0
while count < 300:
    nome = input('qual seu nome? ')
    cidade = input('de que area voce é: ').lower()
    if cidade == 'flamengo':
        flamengo = flamengo + 1
    elif cidade == 'vasco':
        vasco = vasco + 1
    elif cidade == 'cocacola':
        cocacola = cocacola + 1
    count = count + 1

print(flamengo, vasco, cocacola)