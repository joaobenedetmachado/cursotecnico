criciuma = 0
tubarao = 0
lages = 0
count = 0
while count < 50:
    nome = input('qual seu nome? ')
    cidade = input('de que cidade voce é: ').lower()
    if cidade == 'criciuma':
        criciuma = criciuma + 1
    elif cidade == 'tubarao':
        tubarao = tubarao + 1
    elif cidade == 'lages':
        lages = lages + 1
    count = count + 1

print(criciuma, tubarao, lages)