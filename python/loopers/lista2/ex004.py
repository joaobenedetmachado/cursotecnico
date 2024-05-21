mecanico = 0
civil = 0
eletrico = 0
count = 0
while count < 300:
    nome = input('qual seu nome? ')
    cidade = input('de que area voce é: ').lower()
    if cidade == 'mecanico':
        mecanico = mecanico + 1
    elif cidade == 'civil':
        civil = civil + 1
    elif cidade == 'eletrico':
        eletrico = eletrico + 1
    count = count + 1

print(mecanico, civil, eletrico)