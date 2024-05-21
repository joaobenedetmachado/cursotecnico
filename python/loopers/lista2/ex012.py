futebol = 0
basquete = 0
tenis = 0
count = 0
while count < 300:
    nome = input('qual seu nome? ')
    cidade = input('de que area voce é: ').lower()
    if cidade == 'futebol':
        futebol = futebol + 1
    elif cidade == 'basquete':
        basquete = basquete + 1
    elif cidade == 'tenis':
        tenis = tenis + 1
    count = count + 1

print(futebol, basquete, tenis)