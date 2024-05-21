chevrolet = 0
fiat = 0
ford = 0
count = 0
while count < 300:
    nome = input('qual seu nome? ')
    cidade = input('de que area voce é: ').lower()
    if cidade == 'chevrolet':
        chevrolet = chevrolet + 1
    elif cidade == 'fiat':
        fiat = fiat + 1
    elif cidade == 'ford':
        ford = ford + 1
    count = count + 1

print(chevrolet, fiat, ford)