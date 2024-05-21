arquitetura = 0
farmacia = 0
medicina = 0
odontologia = 0
count = 0
while count < 100:
    nome = input('qual seu nome? ')
    resposta = input('que curso voce faz: ').lower()
    if resposta == 'arquitetura':
        arquitetura = arquitetura + 1
    elif resposta == 'farmacia':
        farmacia = farmacia + 1
    elif resposta == 'odontologia':
        odontologia = odontologia + 1
    elif resposta == 'medicina':
        medicina = medicina + 1
    count = count + 1

print(arquitetura, farmacia, odontologia, medicina)